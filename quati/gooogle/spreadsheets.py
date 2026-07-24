import gspread
import pandas as pd
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials


def acquire_gsheet_access(auth_credentials, workbook_title, tab_title):
    """
    Authenticate and retrieve a Google Sheets worksheet object.

    Parameters
    ----------
    auth_credentials : str
        Path to the Google service account credentials JSON file.

    workbook_title : str
        Name of the Google Sheets workbook.

    tab_title : str
        Name of the worksheet/tab inside the workbook.

    Returns
    -------
    gspread.models.Worksheet
        Authenticated worksheet object.

    Examples
    --------
    >>> worksheet = acquire_gsheet_access(
    ...     GSHEETS_CREDENTIAL,
    ...     "My Workbook",
    ...     "Data"
    ... )
    """

    credential = ServiceAccountCredentials.from_json_keyfile_name(
        auth_credentials,
        [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ],
    )

    client = gspread.authorize(credential)

    return client.open(workbook_title).worksheet(tab_title)


def retrieve_gsheet_as_df(worksheet, header_index=1):
    """
    Retrieve a Google Sheets worksheet as a pandas DataFrame.

    The worksheet object must be obtained previously using
    acquire_gsheet_access(). This function does not handle
    authentication or worksheet opening.

    Workflow:
        1. Authenticate and open worksheet:

            worksheet = acquire_gsheet_access(
                auth_credentials,
                workbook_title,
                tab_title
            )

        2. Convert worksheet data into DataFrame:

            dataframe = retrieve_gsheet_as_df(worksheet)

    Parameters
    ----------
    worksheet : gspread.models.Worksheet
        Authenticated worksheet object returned by
        acquire_gsheet_access().

    header_index : int, optional
        Row number containing dataframe headers.

        Default:
            1

    Returns
    -------
    pandas.DataFrame
        Worksheet data converted into a pandas DataFrame.

    Examples
    --------
    >>> worksheet = acquire_gsheet_access(
    ...     GSHEETS_CREDENTIAL,
    ...     "My Workbook",
    ...     "Data"
    ... )
    ...
    >>> dataframe = retrieve_gsheet_as_df(
    ...     worksheet
    ... )
    """

    return pd.DataFrame(worksheet.get_all_records(head=header_index))


def remove_gsheet_duplicates(
    worksheet,
    match_columns,
    keep_strategy="first",
    origin_cell="A1",
    boundary_cell="ZZ",
):
    """
    Remove duplicated records from a Google Sheets worksheet.

    The worksheet object must be authenticated and retrieved previously
    using acquire_gsheet_access(). This function only performs data
    manipulation and worksheet updates.

    Workflow:
        1. Authenticate and retrieve worksheet:

            worksheet = acquire_gsheet_access(
                auth_credentials,
                workbook_title,
                tab_title
            )

        2. Remove duplicated records:

            dataframe = remove_gsheet_duplicates(
                worksheet,
                match_columns=["id"]
            )

    Parameters
    ----------
    worksheet : gspread.models.Worksheet
        Authenticated worksheet object returned by
        acquire_gsheet_access().

    match_columns : str or list
        Column name(s) used to identify duplicated records.

    keep_strategy : str or bool, optional
        Defines which duplicated record should be kept.

        Options:
            - "first": keep first occurrence.
            - "last": keep last occurrence.
            - False: remove all duplicated records.

        Default:
            "first"

    origin_cell : str, optional
        Initial cell where cleaned data will be written.

        Default:
            "A1"

    boundary_cell : str, optional
        Final cell used when clearing the worksheet before update.

        Default:
            "ZZ"

    Returns
    -------
    pandas.DataFrame
        Clean dataframe after duplicated rows removal.

    Examples
    --------
    >>> worksheet = acquire_gsheet_access(
    ...     GSHEETS_CREDENTIAL,
    ...     "Instagram Data",
    ...     "Posts"
    ... )
    ...
    >>> dataframe = remove_gsheet_duplicates(
    ...     worksheet,
    ...     match_columns=["post_id"]
    ... )
    """

    dataframe = retrieve_gsheet_as_df(worksheet)

    dataframe = dataframe.astype(str).drop_duplicates(subset=match_columns, keep=keep_strategy)

    worksheet.batch_clear([f"{origin_cell}:{boundary_cell}"])

    worksheet.update(
        origin_cell,
        dataframe.values.tolist(),
        value_input_option="USER_ENTERED",
    )

    return dataframe


def locate_next_empty_cell(worksheet, col_letter):
    """
    Return the next available cell position in a worksheet column.

    Parameters
    ----------
    worksheet : gspread.models.Worksheet
        Authenticated worksheet object.

    col_letter : str
        Column letter to evaluate.

    Returns
    -------
    str
        Next available cell reference.

    Example
    -------
    >>> locate_next_empty_cell(
    ...     worksheet,
    ...     "A"
    ... )

    Returns:
        A237
    """

    filled_entries = list(filter(None, worksheet.col_values(2)))

    return f"{col_letter}{len(filled_entries) + 1}"


def push_df_to_gsheet(worksheet, source_df, anchor_cell):
    """
    Upload a dataframe into Google Sheets.

    Parameters
    ----------
    worksheet : gspread.models.Worksheet
        Authenticated worksheet object.

    source_df : pandas.DataFrame
        Dataframe to upload.

    anchor_cell : str
        Starting cell for data insertion.

    Returns
    -------
    None
    """

    formatted_df = source_df.astype(str)

    worksheet.update(
        anchor_cell,
        formatted_df.values.tolist(),
        value_input_option="USER_ENTERED",
    )


def safe_open_tab(client, book_name, tab_name, limit=5, wait=60):
    """
    Open worksheet with retry logic.

    Parameters
    ----------
    client : gspread.Client
        Authenticated Google Sheets client.

    book_name : str
        Workbook name.

    tab_name : str
        Worksheet name.

    limit : int
        Maximum retry attempts.

    wait : int
        Waiting time between attempts.

    Returns
    -------
    gspread.models.Worksheet
        Worksheet object.
    """

    attempt = 0

    while attempt < limit:

        try:
            return client.open(book_name).worksheet(tab_name)

        except Exception as error:

            attempt += 1

            print(f"Attempt {attempt} failed: {error}")

            if attempt < limit:
                sleep(wait)
            else:
                raise


def safe_open_tab_by_url(client, link, tab_name, limit=5, wait=60):
    """
    Open worksheet by URL with retry logic.

    Parameters
    ----------
    client : gspread.Client
        Authenticated Google Sheets client.

    link : str
        Spreadsheet URL.

    tab_name : str
        Worksheet name.

    limit : int
        Maximum retry attempts.

    wait : int
        Waiting time between attempts.

    Returns
    -------
    gspread.models.Worksheet
        Worksheet object.
    """

    attempt = 0

    while attempt < limit:

        try:
            return client.open_by_url(link).worksheet(tab_name)

        except Exception as error:

            attempt += 1

            print(f"Attempt {attempt} failed: {error}")

            if attempt < limit:
                sleep(wait)
            else:
                raise


def fetch_records_with_resilience(worksheet, limit=5, wait=60, header_row=0, use_header=True):
    """
    Fetch worksheet records with retry logic.

    Parameters
    ----------
    worksheet : gspread.models.Worksheet
        Worksheet object.

    limit : int
        Retry attempts.

    wait : int
        Waiting time.

    header_row : int
        Header row index.

    use_header : bool
        Whether to use header row.

    Returns
    -------
    pandas.DataFrame
        Worksheet data.
    """

    attempt = 0

    while attempt < limit:

        try:

            rows = worksheet.get_all_values()

            if use_header:

                return pd.DataFrame(rows[1:], columns=rows[header_row])

            return pd.DataFrame(rows)

        except Exception as error:

            attempt += 1

            if attempt < limit:
                sleep(wait)
            else:
                raise Exception(f"Fetch failed: {error}")


def find_next_row_with_resilience(worksheet, col_index=1, limit=4, wait=60):
    """
    Find next empty row in worksheet column.

    Parameters
    ----------
    worksheet : gspread.models.Worksheet
        Worksheet object.

    col_index : int
        Column index.

    Returns
    -------
    int
        Next available row.
    """

    attempt = 0

    while attempt < limit:

        try:

            values = worksheet.col_values(col_index)

            return len(list(filter(None, values))) + 1

        except Exception as error:

            attempt += 1

            if attempt < limit:
                sleep(wait)
            else:
                raise Exception(f"Row detection failed: {error}")


def safe_worksheet_update(worksheet, target_cell, data_df, limit=5, wait=60):
    """
    Update worksheet with dataframe data using retries.

    Parameters
    ----------
    worksheet : gspread.models.Worksheet
        Worksheet object.

    target_cell : str
        Starting cell.

    data_df : pandas.DataFrame
        Dataframe to upload.

    Returns
    -------
    None
    """

    attempt = 0

    while attempt < limit:

        try:

            worksheet.update(
                target_cell,
                data_df.values.tolist(),
                value_input_option="RAW",
            )

            print("Sync complete.")

            return

        except Exception as error:

            attempt += 1

            if attempt < limit:
                sleep(wait)
            else:
                raise Exception(f"Update failed: {error}")
