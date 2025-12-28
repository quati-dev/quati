# fmt: off

# =========================
# PIPELINE PREFIXES
# =========================
PIPE_EXTRACT   = "EXTRACT".ljust(10)
PIPE_TRANSFORM = "TRANSFORM".ljust(10)
PIPE_LOAD      = "LOAD".ljust(10)
PIPE_SPLIT     = "".center(5)

# =========================
# LOG LEVELS
# =========================
LOG_DEBUG = "DEBUG"
LOG_INFO  = "INFO"
LOG_ERROR = "ERROR"

# =========================
# ETL STATUS
# =========================
ETL_SUCCESS     = "SUCCESS"
ETL_FAILURE     = "FAILURE"
ETL_IN_PROGRESS = "IN PROGRESS"

# =========================
# ERROR MESSAGES
# =========================
ERROR_API_AUTH_FAILED        = "API authentication failed. Check your credentials"
ERROR_API_ENDPOINT_NOT_FOUND = "API endpoint not found. Verify the URL"
ERROR_API_FAILED             = "Failed to retrieve data from the API"
ERROR_API_LIMIT_EXCEEDED     = "API rate limit exceeded. Please try again later"
ERROR_API_TIMEOUT            = "API request timed out. Check your network connection"

ERROR_DB_CONNECTION_FAILED   = "Database connection failed"
ERROR_DB_QUERY               = "Error executing a database query"

ERROR_FILE_NOT_FOUND         = "The specified file was not found"
ERROR_FILE_READ              = "Error reading data from the file"
ERROR_FILE_WRITE             = "Error writing data to the file"

ERROR_ETL_CONFIG             = "ETL configuration error"
ERROR_ETL_PROCESS            = "ETL process failed"
ERROR_ETL_DATA_LOAD          = "Data load process failed"
ERROR_ETL_DATA_TRANSFORM     = "Data transformation failed"

ERROR_SELENIUM_AUTH           = "Selenium authentication failed. Check your credentials"
ERROR_SELENIUM_BROWSER        = "Selenium browser encountered an error"
ERROR_SELENIUM_DRIVER_MISSING = "Selenium WebDriver not found at the specified path"
ERROR_SELENIUM_ELEMENT        = "Selenium element not found on the web page"
ERROR_SELENIUM_TIMEOUT        = "Selenium operation timed out"

# =========================
# SUCCESS MESSAGES
# =========================
SUCCESS_API_AUTH              = "API authentication successful"
SUCCESS_API_DATA_CREATED      = "New data successfully created via the API"
SUCCESS_API_DATA_RETRIEVED    = "Data successfully retrieved from the API"
SUCCESS_API_DATA_UPDATED      = "Data successfully updated via the API"

SUCCESS_DB_CONNECTED          = "Database connection established successfully"
SUCCESS_DB_QUERY_EXECUTED     = "Database query executed successfully"

SUCCESS_FILE_READ             = "Data successfully read from the file"
SUCCESS_FILE_WRITE            = "Data successfully written to the file"

SUCCESS_ETL_CONFIG_VALID      = "ETL configuration validated successfully"
SUCCESS_ETL_PROCESS_COMPLETED = "ETL process completed successfully"
SUCCESS_ETL_DATA_LOADED       = "Data loaded into the destination successfully"
SUCCESS_ETL_DATA_TRANSFORMED  = "Data transformation completed successfully"

SUCCESS_SELENIUM_AUTH         = "Selenium authentication successful"
SUCCESS_SELENIUM_ELEMENT      = "Selenium element found on the web page"
SUCCESS_SELENIUM_OPERATION    = "Selenium operation completed successfully"

# =========================
# STATUS / PROCESS
# =========================
STATUS_SELENIUM_OPEN_BROWSER   = "Opening browser"
STATUS_SELENIUM_GO_TO_PAGE     = "Accessing page"
STATUS_SELENIUM_REFRESH_PAGE   = "Refreshing page"
STATUS_SELENIUM_IMPORT_COOKIES = "Importing cookies"

STATUS_INSTAGRAM_BIO           = "Extracting bio text"
STATUS_INSTAGRAM_FOLLOWERS     = "Extracting followers count"
STATUS_INSTAGRAM_FOLLOWING     = "Extracting following count"
STATUS_INSTAGRAM_POSTS         = "Extracting posts count"

STATUS_INSTAGRAM_POST_ID        = "Extracting post ID"
STATUS_INSTAGRAM_POST_DATE      = "Extracting post date"
STATUS_INSTAGRAM_POST_DESC      = "Extracting post description"
STATUS_INSTAGRAM_POST_IMAGE     = "Extracting post image"
STATUS_INSTAGRAM_POST_URL       = "Extracting post URL"
STATUS_INSTAGRAM_POST_LIKES     = "Extracting post likes count"
STATUS_INSTAGRAM_POST_VIEWS     = "Extracting post views count"
STATUS_INSTAGRAM_POST_COMMENTS  = "Extracting post comments count"

# =========================
# PANDAS
# =========================
STATUS_PANDAS_INIT_DF          = "Initializing dataframe"
STATUS_PANDAS_LOAD_CSV         = "Loading data from CSV"
STATUS_PANDAS_SAVE_CSV         = "Saving data to CSV"
STATUS_PANDAS_FILTER           = "Filtering data"
STATUS_PANDAS_GROUP            = "Grouping data"
STATUS_PANDAS_MERGE            = "Merging data"
STATUS_PANDAS_JOIN             = "Joining data"
STATUS_PANDAS_AGGREGATE        = "Aggregating data"
STATUS_PANDAS_DROP_DUPLICATES  = "Dropping duplicates"
STATUS_PANDAS_HANDLE_MISSING   = "Handling missing values"
STATUS_PANDAS_FILL_NA          = "Filling NA values"
STATUS_PANDAS_CONVERT_TYPES    = "Converting data types"
STATUS_PANDAS_REORDER_COLUMNS  = "Reordering columns"
STATUS_PANDAS_TREAT_CHARS      = "Treating characters"
STATUS_PANDAS_ANALYZE_STATS    = "Analyzing statistics"
STATUS_PANDAS_CREATE_VISUALS   = "Creating visualizations"

# =========================
# API PROCESS
# =========================
STATUS_API_REQUEST_START     = "Starting API request"
STATUS_API_SEND_REQUEST      = "Sending API request"
STATUS_API_RECEIVE_RESPONSE  = "Receiving API response"
STATUS_API_PROCESS_RESPONSE  = "Processing API response"
STATUS_API_VALIDATE_RESPONSE = "Validating API response"
STATUS_API_FETCH_DATA        = "Fetching data from API"
STATUS_API_SAVE_DATA         = "Saving API data"
STATUS_API_CACHE_RESPONSE    = "Caching API response"
STATUS_API_UPDATE_CACHE      = "Updating cache"

# =========================
# GOOGLE SHEETS
# =========================
STATUS_GSHEET_GET_SHEET       = "Getting data from sheet"
STATUS_GSHEET_GET_SPREADSHEET = "Getting data from spreadsheet"
STATUS_GSHEET_UPDATE_SHEET    = "Updating sheet data"

# =========================
# BIGQUERY
# =========================
STATUS_BQ_GET_PROJECT    = "Getting data from project"
STATUS_BQ_GET_DATASET    = "Getting data from dataset"
STATUS_BQ_GET_TABLE      = "Getting data from table"
STATUS_BQ_UPDATE_PROJECT = "Updating project data"
STATUS_BQ_UPDATE_DATASET = "Updating dataset data"
STATUS_BQ_UPDATE_TABLE   = "Updating table data"
