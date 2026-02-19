# Header

Defines constants and functions for managing ETL (Extract, Transform, Load) processes, date and time formatting, logging levels, API scopes, database connections, and various data operations.

`Text Constants for ETL Phases`, `Google Sheets API Scope`, `Date and Time`, `Paths and File Locations`, `Database Connection`, `Data Sources`, `Miscellaneous Constants`, `Logging Levels`, `Email Configuration`, `ETL Process Status`, `Data Formats and Locations`, `ETL Configuration`, `Error Handling`, `Throttling and Rate Limits`, `Security`, `Data Export and Serialization`, `File Encoding`, `Data Validation`, `AWS S3 Paths`, `Encryption`, `Data Export Formats`, `Data Backup`, `Data Sampling`

---

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