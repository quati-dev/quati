import pandas as pd
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account


def sync_dataframe_to_bq_schema(
    df_input, target_project, bq_table_id, auth_json, verbose=False, cast_ids_as_string: bool = False
):
    """
    Synchronize the data types of a Pandas DataFrame with a BigQuery table's schema.

    This function takes a Pandas DataFrame, a BigQuery table's schema, and updates the data types
    of the DataFrame columns to match the corresponding schema in the BigQuery table.

    Args
    ----
        - `df_input` (pd.DataFrame): The DataFrame whose data types need to be synchronized.
        - `target_project` (str): The Google Cloud Project ID where the BigQuery table is located.
        - `bq_table_id` (str): The name of the BigQuery table to retrieve the schema from.
        - `auth_json` (str): Path to the service account credential file for authentication.
        - `verbose` (bool, optional): Whether to print debug information (default is False).

    Returns
    -------
        - `pd.DataFrame`: The DataFrame with synchronized data types.

    Examples
    --------
        >>> # Synchronize data types with a BigQuery table
        synced_df = sync_dataframe_to_bq_schema(
            df, 'your_project_id', 'your_dataset.your_table',
            'path/to/your/credential_file.json', verbose=True
        )
    """
    pandas_gbq.context.project = target_project
    bq_client = bigquery.Client(
        credentials=service_account.Credentials.from_service_account_file(auth_json),
        project=target_project,
    )
    remote_table = bq_client.get_table(bq_table_id)

    schema_definitions = [{"field": item.name, "dtype": item.field_type} for item in remote_table.schema]

    type_mapping = {
        "BOOLEAN": bool,
        "FLOAT": float,
        "INTEGER": int,
        "OBJECT": str,
        "STRING": str,
    }

    iso_date_fmt = "%Y-%m-%d"
    iso_timestamp_fmt = "%Y-%m-%d %H:%M:%S:%f"

    for entry in schema_definitions:
        name = entry["field"]
        kind = entry["dtype"]

        if verbose:
            print(entry)

        if kind == "DATE":
            df_input[name] = pd.to_datetime(df_input[name], format=iso_date_fmt, errors="coerce")
        elif kind == "TIMESTAMP":
            df_input[name] = pd.to_datetime(df_input[name], format=iso_timestamp_fmt, errors="ignore")
        elif cast_ids_as_string and "id" in name:
            df_input[name] = df_input[name].astype(str)
        else:
            df_input[name] = df_input[name].astype(type_mapping[kind])

    return df_input


def execute_bq_fetch(sql_command, gcp_project, key_path):
    """
    Executes a BigQuery SQL query and returns the result as a Pandas DataFrame.

    Parameters:
    sql_command (str): The SQL query to execute on BigQuery.

    Returns:
    pandas.DataFrame or None: The result of the query as a DataFrame if successful,
                              None if there was an error.

    Example:
    >>> query = "SELECT * FROM `my_dataset.my_table` LIMIT 10"
    >>> result = bq_query_with_exception(query)
    [10 rows, 5 columns]
    >>> if result is not None:
    >>>     print(result.head())
          column1 column2 column3 column4 column5
    0      value1  value2  value3  value4  value5
    1      value1  value2  value3  value4  value5
    2      value1  value2  value3  value4  value5
    3      value1  value2  value3  value4  value5
    4      value1  value2  value3  value4  value5
    """
    try:
        credentials_obj = service_account.Credentials.from_service_account_file(key_path)
        client_instance = bigquery.Client(
            credentials=credentials_obj,
            project=gcp_project,
        )

        results_df = client_instance.query(sql_command).to_dataframe()

        print(f" [{len(results_df.index)} rows, {len(results_df.columns)} columns]")
        return results_df

    except Exception as error_msg:
        print(f"\n  ❌ Query error: {repr(error_msg)}")
        return None
