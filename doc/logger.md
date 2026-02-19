# Logger (Log Messages)

This Python file defines error and success messages, log levels, and ETL process statuses. These constants standardize messaging and facilitate debugging and monitoring of the system.

> [!NOTE]
> ```py
> from quati.logger.manager import <LOG_MESSAGE>
> ```

- [`Error`](logger.md#error)
- [`Success`](logger.md#success)
- [`ETL Process Status`](logger.md#etl-process-status)

---

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
