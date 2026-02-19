# User Guide

In these guides you will see input code inside code blocks such as:
```py
from quati.analytics.processing import convert_magnitude_string

convert_magnitude_string("1K")
```
or:
```py
In [1]: from quati.analytics.processing import convert_magnitude_string

In [2]: convert_magnitude_string("1K")
Out[2]: 1000
```
The first block is a standard python input, while in the second the In [1]: indicates the input is inside a notebook.
For example:
```py
In [3]: value = convert_magnitude_string("10M")

In [4]: value
Out[4]: 10000000
```
is equivalent to:
```py
value = convert_magnitude_string("10M")
print(value)
```

<h2>Guides</h2>

**Dataframes** <br>
⠀⠀[**`convert_magnitude_string()`**](data.md#convert_magnitude_string): Transforms string-based magnitude suffixes (K, M, B) into numerical integers <br>
⠀⠀[**`format_column_header()`**](data.md#format_column_header): Normalizes DataFrame column names by handling special characters and casing <br>
**Google** <br>
⠀⠀**BigQuery** <br>
⠀⠀⠀⠀[**`sync_dataframe_to_bq_schema()`**](google.md#sync_dataframe_to_bq_schema): Aligns Pandas DataFrame data types with a specific BigQuery table schema <br>
⠀⠀⠀⠀[**`execute_bq_fetch()`**](google.md#execute_bq_fetch): Runs a BigQuery SQL query and returns the results as a Pandas DataFrame <br>
⠀⠀**Google Sheets** <br>
⠀⠀⠀⠀[**`acquire_gsheet_access()`**](google.md#acquire_gsheet_access): Authorizes and retrieves a Google Sheets worksheet object <br>
⠀⠀⠀⠀[**`retrieve_gsheet_as_df()`**](google.md#retrieve_gsheet_as_df): Imports Google Sheets data directly into a Pandas DataFrame <br>
⠀⠀⠀⠀[**`remove_gsheet_duplicates()`**](google.md#remove_gsheet_duplicates): Deduplicates sheet rows based on specific columns and updates the source <br>
⠀⠀⠀⠀[**`locate_next_empty_cell()`**](google.md#locate_next_empty_cell): Identifies the next available cell ID for data insertion in a column <br>
⠀⠀⠀⠀[**`push_df_to_gsheet()`**](google.md#push_df_to_gsheet): Updates a worksheet using a DataFrame starting from a reference pivot cell <br>
**Messengers & Alerts** <br>
⠀⠀[**`Dispatcher.push_emsg()`**](msger.md#push_emsg): Sends structured HTML alerts (Types: error, warning, note, tip, important) with attachment support <br>
**Headers & Constants** <br>
⠀⠀[**`Text Constants for ETL Phases` · `Google Sheets API Scope` · `Date and Time` · `Paths and File Locations` · `Database Connection` · `Data Sources` · `Miscellaneous Constants` · `Logging Levels` · `Email Configuration` · `ETL Process Status` · `Data Formats and Locations` · `ETL Configuration` · `Error Handling` · `Throttling and Rate Limits` · `Security` · `Data Export and Serialization` · `File Encoding` · `Data Validation` · `AWS S3 Paths` · `Encryption` · `Data Export Formats` · `Data Backup` · `Data Sampling`**](header.md) <br>
**Log Messages** <br>
⠀⠀[**`Error`**](logger.md#error) · [**`Success`**](logger.md#success) · [**`ETL Process Status`**](logger.md#etl-process-status) <br>
**System Utilities** <br>
⠀⠀[**`erase_file()`**](system.md#erase_file): Removes a specified file from the file system <br>
⠀⠀[**`modify_file_name()`**](system.md#modify_file_name): Renames an existing file based on path and prefix <br>
⠀⠀[**`locate_and_verify_file()`**](system.md#locate_and_verify_file): Searches for a file and validates it against a minimum size threshold <br>
⠀⠀[**`display_timer()`**](system.md#display_timer): Implements a wait period with an optional visual progress bar <br>
⠀⠀[**`fetch_host_details()`**](system.md#fetch_host_details): Extracts detailed system architecture and kernel information <br>
**Web Scrapping** <br>
⠀⠀[**`launch_navigator()`**](navigation.md#launch_navigator): Initializes a customized Chrome WebDriver instance <br>
⠀⠀[**`save_session_cookies()`**](navigation.md#save_session_cookies): Exports active browser session cookies to a local file <br>
⠀⠀[**`load_session_cookies()`**](navigation.md#load_session_cookies): Injects saved cookies into the browser to bypass authentication <br>
⠀⠀[**`is_node_present()`**](navigation.md#is_node_present): Validates the existence of a web element using XPath <br>
⠀⠀[**`dismiss_popup()`**](navigation.md#dismiss_popup): Automates popup closure via ESC key or targeted element clicks <br>

<hr>

## Dataframes
Provides methods to quickly adjust dataframes.

```py
from quati.data.processing import <FUNCTION>
```

- [**`convert_magnitude_string()`**](data.md#convert_magnitude_string): Transforms string-based magnitude suffixes (K, M, B) into numerical integers
- [**`format_column_header()`**](data.md#format_column_header): Normalizes DataFrame column names by handling special characters and casing

### `convert_magnitude_string()`
The `convert_magnitude_string()` function converts string-based number values (like "1K" or "10.3M") into their corresponding numerical values. It’s useful for normalizing data inputs with suffixes like "K" for thousand, "M" for million, etc.

```py
In [1]: convert_magnitude_string("1K")
Out[1]: 1000

In [2]: convert_magnitude_string("550.1K")
Out[2]: 550100

In [3]: convert_magnitude_string("10.3M")
Out[3]: 10300000
```

### `format_column_header()`
The `format_column_header()` function renames DataFrame columns using a standardized normalization logic. It removes accents, replaces special characters with underscores, and enforces lowercase, ensuring consistent column naming across different sources.

```py
In [1]: 
    Col_A    Cól-B_    cOl__C    col_d
0       3        ar        zz       11
1      12        tg        aa       22

In [2]: df.columns = [format_column_header(c) for c in df.columns]
Out[2]: 
    col_a    col_b    col_c    col_d
0       3       ar       zz       11
1      12       tg       aa       22
```
<hr>

## Google
Provides methods to interact with Google resources such as Sheets and BigQuery to boost data manipulation.

```py
from quati.gooogle.warehouse import <FUNCTION>
```

- [**`sync_dataframe_to_bq_schema()`**](google.md#sync_dataframe_to_bq_schema): Aligns Pandas DataFrame data types with a specific BigQuery table schema
- [**`execute_bq_fetch()`**](google.md#execute_bq_fetch): Runs a BigQuery SQL query and returns the results as a Pandas DataFrame

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

```py
from quati.gooogle.spreadsheets import <FUNCTION>
```

- [**`acquire_gsheet_access()`**](google.md#acquire_gsheet_access): Authorizes and retrieves a Google Sheets worksheet object
- [**`retrieve_gsheet_as_df()`**](google.md#retrieve_gsheet_as_df): Imports Google Sheets data directly into a Pandas DataFrame
- [**`remove_gsheet_duplicates()`**](google.md#remove_gsheet_duplicates): Deduplicates sheet rows based on specific columns and updates the source
- [**`locate_next_empty_cell()`**](google.md#locate_next_empty_cell): Identifies the next available cell ID for data insertion in a column
- [**`push_df_to_gsheet()`**](google.md#push_df_to_gsheet): Updates a worksheet using a DataFrame starting from a reference pivot cell

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
In [1]: next_cell = locate_next_empty_cell(worksheet, "B")
Out[1]: 'B452'
```

### `push_df_to_gsheet()`
The `push_df_to_gsheet()` function synchronizes a DataFrame with a worksheet starting from a specific anchor cell (e.g., 'A1' or 'C10').

```py
In [1]: push_df_to_gsheet(worksheet, stats_df, "A2")
```
<hr>

## Messengers & Alerts
Provides a class to send styled alerts and informational emails from just a few lines of code.

```py
from quati.msger.mailing import Dispatcher
```

- [**`Dispatcher`**](#dispatcher-class): Class to send HTML alert emails (types: error, tip, note, important, warning) with detailed context, attachments and metadata.
- [**`push_emsg()`**](#push_emsg-method): Method of `Dispatcher` to trigger the actual sending of the email.

### `Dispatcher` class

The `Dispatcher` class allows you to configure a sender (`account_user`, `access_key`) and default recipients. It sends a rich HTML-formatted alert email with metadata, attachments, and styling based on the selected theme.

#### Initialize email sender
```py
notifier = Dispatcher(
    account_user="your_email@gmail.com",
    access_key="your_app_token",
    default_list=["team@example.com", "devops@example.com"]
)
```

### `push_emsg()` method
The `push_emsg()` method sends a formatted alert email based on the provided type (`error`, `important`, `note`, `tip`, or `warning`), including optional metadata and attachments.

#### Parameters:
- `abstract` (`str`): Short summary of the alert
- `title` (`str`): Email subject/title
- `datetime` (`str`): When the event occurred
- `message` (`str`): Detailed log or traceback
- `context` (`str`): Name of the process or module
- `extra_data` (`dict`, optional): Key-value pairs shown in the email
- `files` (`list[str]`, optional): List of file paths to attach
- `type` (`str`): One of error, tip, note, important, warning
- `recipients` (`list[str]`, optional): Override recipient list

```py
notifier.push_emsg(
    abstract="Daily Reminder",
    title="Friendly Notice",
    datetime="2026-02-18 23:40",
    message="Just a quick reminder about your scheduled activity.",
    context="personal",
    extra_data={"Category": "Routine", "Importance": "Normal"},
    files=["./local_img.png", "..."],
    type="info",
)
```
<hr>

## Web Scrapping
Provides a set of tools for automating browser interactions, allowing you to perform web scraping tasks with minimal code.

```py
from quati.navigation.automation import <FUNCTION>
```

- [**`launch_navigator()`**](navigation.md#launch_navigator): Initializes a customized Chrome WebDriver instance
- [**`save_session_cookies()`**](navigation.md#save_session_cookies): Exports active browser session cookies to a local file
- [**`load_session_cookies()`**](navigation.md#load_session_cookies): Injects saved cookies into the browser to bypass authentication
- [**`is_node_present()`**](navigation.md#is_node_present): Validates the existence of a web element using XPath
- [**`dismiss_popup()`**](navigation.md#dismiss_popup): Automates popup closure via ESC key or targeted element clicks

### `launch_navigator()`
The `launch_navigator()` function initializes a Chrome browser instance using Selenium. This function is essential for beginning a web scraping session.

```py
In [1]: path = "path/to/chromedriver"

In [2]: url = "https://www.example.com"

In [3]: browser = launch_navigator(url, path, is_headless=True)
```

### `save_session_cookies()`
The `save_session_cookies()` function exports cookies from the browser to maintain session state, which is useful for accessing authenticated web pages without logging in repeatedly.

```py
In [1]: save_session_cookies("/home/computer/Desktop/google_cookies.pkl", driver)
```

### `load_session_cookies()`
The `load_session_cookies()` function imports cookies into the browser to maintain session state, which is useful for bypassing login screens using previously saved sessions.

```py
In [1]: load_session_cookies("/home/computer/Desktop/", "cookieFile.pkl", driver)
```

### `is_node_present()`
The `is_node_present()` function checks if an element exists on a web page based on the provided XPath. This is useful for verifying the presence of elements before interacting with them.

```py
In [1]: is_node_present(xpath_query="/html/body/div[1]/main/div[1]/svg")
Out[1]: True
```

### `dismiss_popup()`
The `dismiss_popup()` function either presses the ESC key or clicks on a specified element on a web page, depending on the action required. This is useful for closing intrusive pop-ups or handling dynamic overlays.

```py
In [1]: dismiss_popup(target_xpath="//div[@id='modal`**]", use_esc=True)

In [2]: dismiss_popup(target_xpath="//div[@id='modal`**]", element_css_class="close-btn")
```
<hr>

## System Utilities
Provides several methods to use system functionality from just a few lines of code.

```py
from quati.system.unix import <FUNCTION>
```

- [**`erase_file()`**](system.md#erase_file): Removes a specified file from the file system
- [**`modify_file_name()`**](system.md#modify_file_name): Renames an existing file based on path and prefix
- [**`locate_and_verify_file()`**](system.md#locate_and_verify_file): Searches for a file and validates it against a minimum size threshold
- [**`display_timer()`**](system.md#display_timer): Implements a wait period with an optional visual progress bar
- [**`fetch_host_details()`**](system.md#fetch_host_details): Extracts detailed system architecture and kernel information using the 'uname -a' command

### `erase_file()`
The `erase_file()` function deletes a specified file from a given directory. This function is useful for removing files that are no longer needed.
```py
In [1]: erase_file("tmp/finalFolder", "test.csv")
Out[1]: 

In [2]: erase_file("system.xlsx")
Out[2]: 
```

### `modify_file_name()`
The `modify_file_name()` function allows you to rename an existing file from its original name to a new name. It is useful for organizing files or correcting file names.
```py
In [1]: modify_file_name("../Desktop/finalFolder", "test.csv", "newname.csv")
Out[1]: 
```

### `locate_and_verify_file()`
The `locate_and_verify_file()` function searches for the existence of a file within a specified directory. It returns 'True' if the file is found and meets size requirements, or 'False' if it is not. You can set a minimum file size in *bytes* or specify a timeout in seconds.
```py
In [1]: locate_and_verify_file("/home/computer/Desktop/finalFolder", "test", 100, 10)
Out[1]: True

In [2]: locate_and_verify_file("test.json")
Out[2]: 
```

### `display_timer()`
The `display_timer()` function pauses execution for a specified number of seconds. Optionally, a progress bar can be displayed via 'tqdm' to show the remaining time during the wait.
```py
In [1]: display_timer(5)
Out[1]: Waiting 5s: 100%|██████████| 5/5 [00:05<00:00,  1.00s/it]

In [2]: display_timer(5, False)
Out[2]: 
```

### `fetch_host_details()`
The `fetch_host_details()` function retrieves detailed system information by executing the 'uname -a' command and parsing the result into a dictionary.
```py
In [1]: info = fetch_host_details()
        if info:
            print(info['kernel_name'])
            print(info['hostname'])
            print(info['kernel_version'])
            print(info['build_info'])
            print(info['architecture'])
Out[1]: 
Linux
device.hostname
23.78.0-237.gtaV.x86_64
#1 SMP PREEMPT_DYNAMIC Wed Jul 9 21:22:20 UTC 2021
x86_64 x86_64 x86_64 GNU/Linux
```
<hr>

## Logger (Log Messages)
This Python file defines error and success messages, log levels, and ETL process statuses. These constants standardize messaging and facilitate debugging and monitoring of the system.

```py
from quati.logger.manager import <LOG_MESSAGE>
```

- [**`Error`**](logger.md#error)
- [**`Success`**](logger.md#success)
- [**`ETL Process Status`**](logger.md#etl-process-status)

### Error
Grouped for different contexts such as API, Selenium, file operations, data transformation, data loading, and database operations.

-  `API Errors`: Messages related to API failures, rate limits, authentication issues, endpoint errors, and timeouts.
-  `Selenium Errors`: Messages for WebDriver issues, element not found, authentication failures, timeouts, and browser errors.
-  `File Operations Errors`: Messages for file not found, read/write errors.
-  `Data Errors`: Messages for data transformation and loading failures.
-  `Database Errors`: Messages for connection and query errors.
-  `ETL Errors`: Messages for ETL process and configuration failures.

### Success
Indicate successful completion of various operations such as API, Selenium, file operations, data transformation, data loading, and database operations.
Log Levels

Categorize the importance and nature of messages during program execution.:
- `LOG_LEVEL_INFO`
- `LOG_LEVEL_ERROR`
- `LOG_LEVEL_DEBUG`

### ETL Process Status
Indicate the current state of the ETL process.

- `ETL_STATUS_SUCCESS`
- `ETL_STATUS_FAILURE`
- `ETL_STATUS_IN_PROGRESS`

<hr>

## Header
Defines constants and functions for managing ETL (Extract, Transform, Load) processes, date and time formatting, logging levels, API scopes, database connections, and various data operations.

`Text Constants for ETL Phases`, `Google Sheets API Scope`, `Date and Time`, `Paths and File Locations`, `Database Connection`, `Data Sources`, `Miscellaneous Constants`, `Logging Levels`, `Email Configuration`, `ETL Process Status`, `Data Formats and Locations`, `ETL Configuration`, `Error Handling`, `Throttling and Rate Limits`, `Security`, `Data Export and Serialization`, `File Encoding`, `Data Validation`, `AWS S3 Paths`, `Encryption`, `Data Export Formats`, `Data Backup`, `Data Sampling`

### Text Constants for ETL Phases
- `E_PREFIX`, `T_PREFIX`, `L_PREFIX`: Used to label different phases of the ETL process.
- `STR_SPLIT`, `STR_SPLIT2`: String constants for formatting purposes.

### Google Sheets API Scope
- `GSHEETS_SCOPE`: Scope URLs for accessing Google Sheets and Google Drive APIs.

### Date and Time
#### *Formats*
- `DATE_FORMAT`, `TIME_FORMAT`, `DATETIME_FORMAT`: Standard formats for date, time, and datetime.

#### *Setters*
- `NOW`: Current datetime object.
- `JOBDATE_DATE_FORMAT`, `JOBDATE_TIME_FORMAT`, `JOBDATE_DATETIME_FORMAT`: Current date, time, and datetime in the specified formats.

### Paths and File Locations
- `CHROMEDRIVER_PATH`: Path to the ChromeDriver executable.
- `LOG_FILE`, `CONFIG_FILE`: Paths to the log file and configuration file.

### Database Connection
- `DB_HOST`, `DB_PORT`: Database host and port configuration.

### Data Sources
- `DATA_SOURCE_API`: URL for the API data source.
- `DATA_SOURCE_FILE`: Path to the local data file.

### Miscellaneous Constants
- `MAX_RETRIES`: Maximum number of retries for operations.
- `DEFAULT_TIMEOUT`: Default timeout duration.
- `DEBUG_MODE`: Flag to enable or disable debug mode.

### Logging Levels
- `LOG_LEVEL_INF`, `LOG_LEVEL_ERRO`, `LOG_LEVEL_DEBU`, `LOG_LEVEL_WARNIN`: Different logging levels.

### Email Configuration
- `SMTP_SERVE`, `SMTP_POR`, `SMTP_USERNAM`, `SMTP_PASSWOR`: SMTP server configuration for email notifications.

### ETL Process Status
- `ETL_STATUS_SUCCES`, `ETL_STATUS_FAILUR`, `ETL_STATUS_IN_PROGRES`: Status indicators for the ETL process.

### Data Formats and Locations
- `CSV_FILE_FORMA`, `JSON_FILE_FORMA`, `XML_FILE_FORMA`, `XLSX_FILE_FORMA`: Supported data file formats.
- `RAW_DATA_DI`, `PROCESSED_DATA_DI`: Directories for raw and processed data.

### ETL Configuration
- `MAX_RECORDS_PER_LOAD`: Maximum records to load per operation.
- `NULL_REPLACEMENT`, `DUPLICATE_STRATEGY`: Data cleaning strategies.

### Error Handling
- `ERROR_LOG_FILE`: Path to the error log file.
- `ERROR_THRESHOLD`: Threshold for error tolerance.

### Throttling and Rate Limits
- `API_REQUESTS_PER_MINUTE`: API request rate limit.

### Security
- `GCP_KEYFILE_SPOTIFY`: Path to the Google Cloud Platform keyfile for Spotify.

### Data Export and Serialization
- `EXPORT_PATH`: Path for exported data.
- `PICKLE_FILE_FORMAT`, `PARQUET_FILE_FORMAT`: Data serialization formats.
- `GZIP_FILE_FORMAT`, `TAR_ILE_FORMAT`, `ZIP_FILE_FORMAT`: Data compression formats.

### File Encoding
- `ENCODING_UTF8`, `ENCODING_LATIN1`: Supported file encodings.

### Data Validation
- `DATA_VALIDATION_THRESHOLD`: Threshold for data validation.

### AWS S3 Paths
- `S3_RAW_DATA_PREFIX`, `S3_PROCESSED_DATA_PREFIX`: S3 prefixes for raw and processed data.

### Encryption
`ENCRYPTION_KEY`: Key for data encryption.

### Data Export Formats
`PDF_FILE_FORMAT`, XLSX_FILE_FORMAT: Supported export formats.

### Data Backup
- `BACKUP_DIR`: Directory for data backups.

### Data Sampling
- `SAMPLE_SIZE`: Proportion of data to sample.

[⇧ Go to Top](#table-of-contents)