# Features & Functions

## *Dataframes*
Provides methods to quickly adjust dataframes.

> [!NOTE]
> ```py
> from quati.data.processing import <FUNCTION>
> ```

- [`convert_magnitude_string()`](data.md#convert_magnitude_string): Transforms string-based magnitude suffixes (K, M, B) into numerical integers
- [`format_column_header()`](data.md#format_column_header): Normalizes DataFrame column names by handling special characters and casing

## *Google*
Provides methods to interact with Google resources such as Sheets and BigQuery to boost data manipulation.

### *BigQuery*

> [!NOTE]
> ```py
> from quati.gooogle.warehouse import <FUNCTION>
> ```

- [`sync_dataframe_to_bq_schema()`](google.md#sync_dataframe_to_bq_schema): Aligns Pandas DataFrame data types with a specific BigQuery table schema
- [`execute_bq_fetch()`](google.md#execute_bq_fetch): Runs a BigQuery SQL query and returns the results as a Pandas DataFrame

### *Google Sheets*

> [!NOTE]
> ```py
> from quati.gooogle.spreadsheets import <FUNCTION>
> ```

- [`acquire_gsheet_access()`](google.md#acquire_gsheet_access): Authorizes and retrieves a Google Sheets worksheet object
- [`retrieve_gsheet_as_df()`](google.md#retrieve_gsheet_as_df): Imports Google Sheets data directly into a Pandas DataFrame
- [`remove_gsheet_duplicates()`](google.md#remove_gsheet_duplicates): Deduplicates sheet rows based on specific columns and updates the source
- [`locate_next_empty_cell()`](google.md#locate_next_empty_cell): Identifies the next available cell ID for data insertion in a column
- [`push_df_to_gsheet()`](google.md#push_df_to_gsheet): Updates a worksheet using a DataFrame starting from a reference pivot cell

## *Messengers & Alerts*
Provides a class to send styled alerts and informational emails from just a few lines of code.

> [!NOTE]
> ```py
> from quati.msger.mailing import Dispatcher
> ```

- [`Dispatcher.push_emsg()`](msger.md#push_emsg): Sends structured HTML alerts (Types: error, warning, note, tip, important) with attachment support

## *Headers & Constants*
Defines constants and functions for managing ETL (Extract, Transform, Load) processes, date and time formatting, logging levels, API scopes, database connections, and various data operations.

> [!NOTE]
> ```py
> from quati.header.manager import <ITEM>
> ```

[`Text Constants for ETL Phases` • `Google Sheets API Scope` • `Date and Time` • `Paths and File Locations` • `Database Connection` • `Data Sources` • `Miscellaneous Constants` • `Logging Levels` • `Email Configuration` • `ETL Process Status` • `Data Formats and Locations` • `ETL Configuration` • `Error Handling` • `Throttling and Rate Limits` • `Security` • `Data Export and Serialization` • `File Encoding` • `Data Validation` • `AWS S3 Paths` • `Encryption` • `Data Export Formats` • `Data Backup` • `Data Sampling`](header.md)

## *Log Messages*
This Python file defines error and success messages, log levels, and ETL process statuses. These constants standardize messaging and facilitate debugging and monitoring of the system.

> [!NOTE]
> ```py
> from quati.logger.manager import <LOG_MESSAGE>
> ```

[`Error`](logger.md#error) • [`Success`](logger.md#success) • [`ETL Process Status`](logger.md#etl-process-status)

## *System Utilities*
Provides several methods to use system functionality from just a few lines of code.

> [!NOTE]
> ```py
> from quati.system.unix import <FUNCTION>
> ```

- [`erase_file()`](system.md#erase_file): Removes a specified file from the file system
- [`modify_file_name()`](system.md#modify_file_name): Renames an existing file based on path and prefix
- [`locate_and_verify_file()`](system.md#locate_and_verify_file): Searches for a file and validates it against a minimum size threshold
- [`display_timer()`](system.md#display_timer): Implements a wait period with an optional visual progress bar
- [`fetch_host_details()`](system.md#fetch_host_details): Extracts detailed system architecture and kernel information

## *Web Scrapping*
Provides a set of tools for automating browser interactions, allowing you to perform web scraping tasks with minimal code.

### *Selenium*

> [!NOTE]
> ```py
> from quati.navigation.automation import <FUNCTION>
> ```

- [`launch_navigator()`](navigation.md#launch_navigator): Initializes a customized Chrome WebDriver instance
- [`save_session_cookies()`](navigation.md#save_session_cookies): Exports active browser session cookies to a local file
- [`load_session_cookies()`](navigation.md#load_session_cookies): Injects saved cookies into the browser to bypass authentication
- [`is_node_present()`](navigation.md#is_node_present): Validates the existence of a web element using XPath
- [`dismiss_popup()`](navigation.md#dismiss_popup): Automates popup closure via ESC key or targeted element clicks

<hr>

[⇧ Go to Top](#table-of-contents)