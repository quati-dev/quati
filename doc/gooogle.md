# Google

Provides methods to interact with Google resources such as Sheets and BigQuery to boost data manipulation.

> [!NOTE]
> ```py
> from quati.gooogle.warehouse import <FUNCTION>
> ```

- [`sync_dataframe_to_bq_schema()`](google.md#sync_dataframe_to_bq_schema): Aligns Pandas DataFrame data types with a specific BigQuery table schema
- [`execute_bq_fetch()`](google.md#execute_bq_fetch): Runs a BigQuery SQL query and returns the results as a Pandas DataFrame

> [!NOTE]
> ```py
> from quati.gooogle.spreadsheets import <FUNCTION>
> ```

- [`acquire_gsheet_access()`](google.md#acquire_gsheet_access): Authorizes and retrieves a Google Sheets worksheet object
- [`retrieve_gsheet_as_df()`](google.md#retrieve_gsheet_as_df): Imports Google Sheets data directly into a Pandas DataFrame
- [`remove_gsheet_duplicates()`](google.md#remove_gsheet_duplicates): Deduplicates sheet rows based on specific columns and updates the source
- [`locate_next_empty_cell()`](google.md#locate_next_empty_cell): Identifies the next available cell ID for data insertion in a column
- [`push_df_to_gsheet()`](google.md#push_df_to_gsheet): Updates a worksheet using a DataFrame starting from a reference pivot cell

---

### `sync_dataframe_to_bq_schema()`
The `sync_dataframe_to_bq_schema()` function ensures that the data types in your local Pandas DataFrame match the schema defined in a BigQuery table. This prevents schema mismatch errors during data uploads.

```py
In [1]: df = sync_dataframe_to_bq_schema(df, "project_id", "dataset.table_name", "creds.json", debug=True)
```

### `execute_bq_fetch()`
The `execute_bq_fetch()` function simplifies data extraction by executing an SQL query on BigQuery and returning a ready-to-use Pandas DataFrame.

```py
In [1]: query = "SELECT * FROM `project.dataset.table` LIMIT 10"
In [2]: df = execute_bq_fetch(query, "project_id", "creds.json")
```

---

### `acquire_gsheet_access()`
The `acquire_gsheet_access()` function establishes a connection and returns a worksheet object. It requires service account credentials and the specific workbook and tab names.

```py
In [1]: wks = acquire_gsheet_access(GSHEETS_CREDENTIAL, "Production_Report", "Daily_Stats")
```

### `retrieve_gsheet_as_df()`
The `retrieve_gsheet_as_df()` function pulls data from a Google Sheet and converts it into a DataFrame in one step, allowing for immediate data analysis.

```py
In [1]: df = retrieve_gsheet_as_df(GSHEETS_CREDENTIAL, "Production_Report", "Daily_Stats", header_index=1)
```

### `remove_gsheet_duplicates()`
The `remove_gsheet_duplicates()` function performs in-place deduplication. it clears the specified range and re-uploads the cleaned DataFrame based on the columns provided for matching.

```py
In [1]: clean_df = remove_gsheet_duplicates(GSHEETS_CREDENTIAL, ["user_id"], "User_Database", "Raw_Data", keep_strategy="last")
```

### `locate_next_empty_cell()`
The `locate_next_empty_cell()` function scans a specific column to find the first empty row, returning the cell coordinate (e.g., 'A237'). This is vital for appending data without data collision.

```py
In  [1]: next_cell = locate_next_empty_cell(worksheet, "B")
Out [1]: 'B452'
```

### `push_df_to_gsheet()`
The `push_df_to_gsheet()` function synchronizes a DataFrame with a worksheet starting from a specific anchor cell (e.g., 'A1' or 'C10').

```py
In [1]: push_df_to_gsheet(worksheet, stats_df, "A2")
```