<div align="center">
	<picture>
	<!-- <source media="(prefers-color-scheme: dark)" srcset="assets/quati_white.svg"> -->
	<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/quati-dev/quati/refs/heads/main/assets/quati.png">
		<img src="https://raw.githubusercontent.com/quati-dev/quati/refs/heads/main/assets/quati.png" width="100%">
	</picture>
	<br><br><br>
	<hr>
<h1>quati: A python <u>Quick Actions Toolkit</u> for data engeneering</h1>

<img src="https://img.shields.io/badge/Author-lucasoal-blue?logo=github&logoColor=white"> <img src="https://img.shields.io/badge/License-MIT-750014.svg"> <!-- <img src="https://img.shields.io/badge/Status-Beta-DF1F72">  -->
<br>
<img src="https://img.shields.io/pypi/v/quati.svg?label=Version&color=white"> <img src="https://img.shields.io/pypi/pyversions/quati?logo=python&logoColor=white&label=Python"> <img src="https://img.shields.io/badge/Code Style-Black Formatter-111.svg"> 
<br>
<img src="https://static.pepy.tech/badge/quati/month">
<!-- <img src="https://static.pepy.tech/badge/quati"> -->
<!-- <img src="https://img.shields.io/pypi/dm/quati.svg?label=PyPI downloads"> -->

</div>

## What is it?
**quati** is a multifaceted utility framework featuring a suite of high-performance
functions engineered to streamline software development and operational automation. 
It encompasses a robust and adaptable infrastructure of **modular tools**, 
**specialized libraries**, and **technical assets**, empowering professionals to
architect, implement, and orchestrate complex applications with heightened precision 
and reduced time-to-market.

<h2>Table of Contents</h2>

- [What is it?](#what-is-it)
- [Main Features](#main-features)
- [Where to get it / Install](#where-to-get-it--install)
- [Documentation](#documentation)
- [License](#license)
- [Dependencies](#dependencies)

## Main Features
Here are just a few of the things that pandas does well:

- [`convert_magnitude_string()`](https://github.com/quati-dev/quati/blob/main/doc/data.md#convert_magnitude_string): Transforms string-based magnitude suffixes (K, M, B) into numerical integers
- [`format_column_header()`](https://github.com/quati-dev/quati/blob/main/doc/data.md#format_column_header): Normalizes DataFrame column names by handling special characters and casing
- [`sync_dataframe_to_bq_schema()`](https://github.com/quati-dev/quati/blob/main/doc/gooogle.md#sync_dataframe_to_bq_schema): Aligns Pandas DataFrame data types with a specific BigQuery table schema
- [`execute_bq_fetch()`](https://github.com/quati-dev/quati/blob/main/doc/gooogle.md#execute_bq_fetch): Runs a BigQuery SQL query and returns the results as a Pandas DataFrame
- [`acquire_gsheet_access()`](https://github.com/quati-dev/quati/blob/main/doc/gooogle.md#acquire_gsheet_access): Authorizes and retrieves a Google Sheets worksheet object
- [`retrieve_gsheet_as_df()`](https://github.com/quati-dev/quati/blob/main/doc/gooogle.md#retrieve_gsheet_as_df): Imports Google Sheets data directly into a Pandas DataFrame
- [`remove_gsheet_duplicates()`](https://github.com/quati-dev/quati/blob/main/doc/gooogle.md#remove_gsheet_duplicates): Deduplicates sheet rows based on specific columns and updates the source
- [`locate_next_empty_cell()`](https://github.com/quati-dev/quati/blob/main/doc/gooogle.md#locate_next_empty_cell): Identifies the next available cell ID for data insertion in a column
- [`push_df_to_gsheet()`](https://github.com/quati-dev/quati/blob/main/doc/gooogle.md#push_df_to_gsheet): Updates a worksheet using a DataFrame starting from a reference pivot cell
- [`Dispatcher.push_emsg()`](https://github.com/quati-dev/quati/blob/main/doc/msger.md#push_emsg): Sends structured HTML alerts (Types: error, warning, note, tip, important) with attachment support
- [`erase_file()`](https://github.com/quati-dev/quati/blob/main/doc/system.md#erase_file): Removes a specified file from the file system
- [`modify_file_name()`](https://github.com/quati-dev/quati/blob/main/doc/system.md#modify_file_name): Renames an existing file based on path and prefix
- [`locate_and_verify_file()`](https://github.com/quati-dev/quati/blob/main/doc/system.md#locate_and_verify_file): Searches for a file and validates it against a minimum size threshold
- [`display_timer()`](https://github.com/quati-dev/quati/blob/main/doc/system.md#display_timer): Implements a wait period with an optional visual progress bar
- [`fetch_host_details()`](https://github.com/quati-dev/quati/blob/main/doc/system.md#fetch_host_details): Extracts detailed system architecture and kernel information
- [`launch_navigator()`](https://github.com/quati-dev/quati/blob/main/doc/navigation.md#launch_navigator): Initializes a customized Chrome WebDriver instance
- [`save_session_cookies()`](https://github.com/quati-dev/quati/blob/main/doc/navigation.md#save_session_cookies): Exports active browser session cookies to a local file
- [`load_session_cookies()`](https://github.com/quati-dev/quati/blob/main/doc/navigation.md#load_session_cookies): Injects saved cookies into the browser to bypass authentication
- [`is_node_present()`](https://github.com/quati-dev/quati/blob/main/doc/navigation.md#is_node_present): Validates the existence of a web element using XPath
- [`dismiss_popup()`](https://github.com/quati-dev/quati/blob/main/doc/navigation.md#dismiss_popup): Automates popup closure via ESC key or targeted element clicks

## Where to get it / Install
The source code is currently hosted on GitHub at: https://github.com/quati-dev/quati


> [!WARNING]
> It's essential to use [**Python 3.10**](https://www.python.org/downloads/release/python-310/) version
<!-- > It's essential to **upgrade pip** to the latest version to ensure compatibility with the library. -->
<!-- > ```sh
> # Requires the latest pip
> pip install --upgrade pip
> ``` -->

- [PyPI](https://pypi.org/project/quati/)
	```sh
	# PyPI
	pip install quati
	```
- GitHub
	```sh
	# or GitHub
	pip install git+https://github.com/quati-dev/quati.git
	```

## Documentation
- [Documentation](https://github.com/quati-dev/quati/blob/main/doc/DOCUMENTATION.md).

## License
- [MIT](https://github.com/quati-dev/quati/blob/main/LICENSE)

## Dependencies
- [NumPy](https://numpy.org/) | [Pandas](https://pandas.pydata.org/) | [Selenium](https://www.automation.dev/) | [gspread](https://docs.gspread.org/)

See the [full installation instructions](https://github.com/quati-dev/quati/blob/main/INSTALLATION.md) for minimum supported versions of required, recommended and optional dependencies.

<hr>

[⇧ Go to Top](#table-of-contents)