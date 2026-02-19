import gspread
import pandas as pd
from time import sleep


def acquire_gsheet_access(auth_credentials, workbook_title, tab_title):
    """
    Import a worksheet object from gsheets

    Parameters
    ----------
    `auth_credentials` : Credentials to authorize project access on the google platform
    `workbook_title` : name of the worksheet you want to get information about
    `tab_title` : sheet page name you want to get data from
    `head_row` : row where data header starts

    By default:----------
        - the function consider row 1 as header_

    Examples
    --------
    Get the Google Sheets worksheet object
    >>> worksheet = acquire_gsheet_access(GSHEETS_CREDENTIAL, "worksheet name", "data page name", 6)
    """
    session = gspread.authorize(auth_credentials)
    target_tab = session.open(workbook_title).worksheet(tab_title)
    return target_tab


def retrieve_gsheet_as_df(auth_credentials, workbook_title, tab_title, header_index=1):
    """
    Import a worksheet object from gsheets as a pandas dataframe

    Parameters
    ----------
    `auth_credentials` : Credentials to authorize project access on the google platform
    `workbook_title` : name of the worksheet you want to get information about
    `tab_title` : sheet page name you want to get data from
    `header_index` : row where data header starts

    By default: the function consider row 1 as header

    Examples
    --------
    Get the Google Sheets worksheet object

    ```
    worksheet = retrieve_gsheet_as_df(GSHEETS_CREDENTIAL, "worksheet name", "data page name", 6)
    ```
    """
    tab_obj = acquire_gsheet_access(auth_credentials, workbook_title, tab_title)
    extracted_data = pd.DataFrame(tab_obj.get_all_records(head=header_index))
    return extracted_data


def remove_gsheet_duplicates(
    auth_credentials,
    match_columns,
    workbook_title,
    tab_title,
    keep_strategy="first",
    origin_cell="A1",
    boundary_cell="ZZ",
):
    """Returns dataframe where the column passed as parameter is considered the core set for duplicate data row remover.

    Parameters
    ----------
    `auth_credentials` : Credentials to authorize project access on the google platform
    `match_columns`: column(s) to consider to check for duplicate data in it
    `workbook_title` : name of the worksheet you want information about
    `tab_title` : sheet page name you want to get data from

    By default:
        - `keep_strategy` : Line 1 as data to be kept
        - `origin_cell` : Cell "A1" as the starting point for dataframe cleaning and reordering
        - `boundary_cell` : The cell "ZZ" as the endpoint for dataframe cleaning and reordering

    Examples
    --------
    Get the Google Sheets worksheet object

    ```
    dedup_df = remove_gsheet_duplicates(GSHEETS_CREDENTIAL, "post_title", "facebook_posts", "all_posts", "last", "A5")
    ```
    """
    tab_instance = gspread.authorize(auth_credentials).open(workbook_title).worksheet(tab_title)
    data_frame = retrieve_gsheet_as_df(auth_credentials, workbook_title, tab_title)

    data_frame = data_frame.astype(str).drop_duplicates(subset=match_columns, keep=keep_strategy)

    tab_instance.batch_clear([f"{origin_cell}:{boundary_cell}"])
    tab_instance.update(
        f"{origin_cell}",
        data_frame.values.tolist(),
        value_input_option="USER_ENTERED",
    )

    return data_frame


def locate_next_empty_cell(tab_obj, col_letter):
    """
    Return the ID of the next cell into which data can be entered

    Parameters
    ----------
    `tab_obj` : the worksheet "object" so that the function can identify the data
    `col_letter` : column which function should be considered to check cell continuity

    Examples
    --------
    Get, from the facebook posts spreadsheet, in the column where the comments of all the posts are, the next line where the new data can be inserted

    ```
    df = locate_next_empty_cell(worksheet, "A")
    A237
    ```
    """
    filled_entries = list(filter(None, tab_obj.col_values(2)))
    target_row = str(len(filled_entries) + 1)
    return str(col_letter + target_row)


def push_df_to_gsheet(tab_obj, source_df, anchor_cell):
    """
    Update a Google Sheets spreadsheet from a reference column

    Parameters
    ----------
    `tab_obj`: the "object" of the worksheet so that the function can identify the data
    `source_df`: the dataframe "object" so the function can transfer to the worksheet
    `anchor_cell`: column which the function must be considered to establish the upload

    Examples
    --------
    Upload the face dataframe data, in the facebook statistics worksheet, considering the pivot column "A3"

    ```
    push_df_to_gsheet(worksheet, facebook_metrics_df, "A3")
    ```
    """
    formatted_df = source_df.astype(str)
    tab_obj.update(
        f"{anchor_cell}",
        formatted_df.values.tolist(),
        value_input_option="USER_ENTERED",
    )


def safe_open_tab(client, book_name, tab_name, limit=5, wait=60):
    """
    Opens a worksheet in a Google Sheets spreadsheet by its name, with retry logic
    to handle potential errors during the operation.

    Args:
        client (gspread.Client): The authenticated gspread client object.
        book_name (str): The name of the Google Sheets spreadsheet to open.
        tab_name (str): The name of the worksheet to access within the spreadsheet.
        limit (int, optional): The maximum number of retry attempts in case of failure. Defaults to 5.
        wait (int, optional): The time (in seconds) to wait between retry attempts. Defaults to 60.

    Returns:
        gspread.models.Worksheet: The worksheet object if successfully opened.

    Raises:
        Exception: If the function fails to open the worksheet after the specified number of retries.

    Example:
        Get spreadsheet named "Planilha do Fulano" on worksheet "Aba teste".

        worksheet = safe_open_tab(gc, "Planilha do Fulano", "Aba Teste")
    """
    step = 0
    while step < limit:
        try:
            return client.open(book_name).worksheet(tab_name)
        except Exception as error:
            step += 1
            print(f"Attempt {step} | Book: {book_name} | Tab: {tab_name} failed: \n{error}")
            if step < limit:
                print(f"Waiting {wait}s...")
                sleep(wait)
            else:
                raise


def safe_open_tab_by_url(client, link, tab_name, limit=5, wait=60):
    """
    Opens a worksheet in a Google Sheets spreadsheet by its URL, with retry logic
    to handle potential errors during the operation.

    Args:
        client (gspread.Client): The authenticated gspread client object.
        link (str): The URL of the Google Sheets spreadsheet.
        tab_name (str): The name of the worksheet to open.
        limit (int, optional): The maximum number of retry attempts in case of failure. Defaults to 5.
        wait (int, optional): The time (in seconds) to wait between retry attempts. Defaults to 60.

    Returns:
        gspread.models.Worksheet: The worksheet object if successfully opened.

    Raises:
        Exception: If the function fails to open the worksheet after the specified number of retries.

    Example:
        Opens by the url specified on sheet "Aba teste".

        worksheet = safe_open_tab_by_url(gc, "https://docs.google.com/spreadsheets/d/XXXXX", "Aba teste")
    """
    step = 0
    while step < limit:
        try:
            return client.open_by_url(link).worksheet(tab_name)
        except Exception as error:
            step += 1
            print(f"Attempt {step} | URL: {link} | Tab: {tab_name} failed: \n{error}")
            if step < limit:
                sleep(wait)
            else:
                raise


def fetch_records_with_resilience(tab_obj, limit=5, wait=60, header_row=0, use_header=True):
    """
    Fetches records from a Google Sheets worksheet and converts them into a Pandas DataFrame,
    with retry logic to handle potential errors during the fetch process.

    Args:
        tab_obj (gspread.models.Worksheet): The worksheet object to fetch records from.
        limit (int, optional): The maximum number of retry attempts in case of failure. Defaults to 5.
        wait (int, optional): The time (in seconds) to wait between retry attempts. Defaults to 60.
        header_row (int, optional): Specifies the row to use for column headers. Defaults to 0 (first row).
        use_header (bool, optional): Whether to use the first row as column headers. Defaults to True.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the fetched records.

    Raises:
        Exception: If the function fails to fetch records after the specified number of retries.

    Example:
        Get data from worksheet as a dataframe, including first row (number 0) as header.

        dataframe = fetch_records_with_resilience(worksheet, header_row=0, use_header=True)

    """
    count = 0
    while count < limit:
        try:
            all_rows = tab_obj.get_all_values()
            if use_header:
                result_df = pd.DataFrame(all_rows[1:], columns=all_rows[header_row])
            else:
                result_df = pd.DataFrame(all_rows)
            return result_df
        except Exception as error:
            count += 1
            if count < limit:
                sleep(wait)
            else:
                raise Exception(f"Fetch failed after {limit} tries. Error: {error}")


def find_next_row_with_resilience(tab_obj, col_index=1, limit=4, wait=60):
    """
    Retrieves the next available row number in a Google Sheets worksheet,
    with retry logic to handle potential failures.

    Args:
        tab_obj (gspread.models.Worksheet): The Google Sheets worksheet object.
        col_index (int, optional): The starting column for checking values. Defaults to 1 (column A).
        limit (int, optional): The maximum number of retry attempts in case of an error. Defaults to 4.
        wait (int, optional): The time (in seconds) to wait between retries. Defaults to 60.

    Returns:
        int: The row number of the next available empty row in the worksheet.

    Raises:
        Exception: If the function fails after the specified number of retries.

    Example:
        Get next available row given a column number.

        next_row = find_next_row_with_resilience(worksheet, col_index=2)
    """
    count = 0
    while count < limit:
        try:
            column_data = tab_obj.col_values(col_index)
            valid_rows = list(filter(None, column_data))
            return len(valid_rows) + 1
        except Exception as error:
            count += 1
            if count < limit:
                sleep(wait)
            else:
                raise Exception(f"Row detection failed. Error: {error}")


def safe_worksheet_update(tab_obj, target_cell, data_df, limit=5, wait=60):
    """
    Updates a Google Sheets worksheet with the provided data,
    using retries to handle potential errors during the update process.

    Args:
        tab_obj (gspread.models.Worksheet): The worksheet object to update.
        target_cell (str): The starting cell or range for the update (e.g., "A12").
                Use `get_next_available_row_with_retry()` to determine available rows based on specific columns.
        data_df (pandas.DataFrame): The data to be inserted, converted to a list of lists.
        limit (int, optional): The maximum number of retry attempts in case of failure. Defaults to 5.
        wait (int, optional): The time (in seconds) to wait between retry attempts. Defaults to 60.

    Returns:
        None

    Raises:
        Exception: If the function fails to update the worksheet after the specified number of retries.

    Example:
        Update worksheet with dataframe data. For the parameter target_cell is highly
        recommended the use of the function find_next_row_with_resilience().

        next_row = find_next_row_with_resilience(worksheet, col_index=2)
            - supose next_row is 5

        target_cell = "B" + str(next_row)
            - then target_cell will be "B5"

        safe_worksheet_update(worksheet, target_cell="B5", dataframe.astype(str))

    """
    count = 0
    while count < limit:
        try:
            tab_obj.update(target_cell, data_df.values.tolist(), value_input_option="RAW")
            print("Sync complete.")
            return
        except Exception as error:
            count += 1
            if count < limit:
                sleep(wait)
            else:
                raise Exception(f"Update failed after {limit} tries. Error: {error}")
