import pandas as pd


def convert_magnitude_string(raw_input: str) -> int:
    """
    Normalize a value that contains characters 'K', 'M', 'B';

    Example
    -------
    ```
    convert_magnitude_string("1K")
    1000
    convert_magnitude_string("550.1K")
    550100
    convert_magnitude_string("10.3M")
    10300000
    ```
    """
    clean_text = raw_input.lower()
    scaling_factors = {"k": 1000, "m": 1000000, "b": 1000000000}

    for suffix, multiplier in scaling_factors.items():
        if suffix in clean_text:
            numeric_value = float(clean_text.replace(suffix, ""))
            return int(numeric_value * multiplier)

    return int(float(clean_text))


import re


def format_column_header(label: str, lowercase: bool = True) -> str:
    """
    Clean and rename a column name by removing special characters, replacing spaces with underscores,
    and optionally converting to lowercase or uppercase.

    Args
    ----
        - `label` (str): The original column name to be cleaned and renamed.
        - `lowercase` (bool, optional): Whether to convert the result to lowercase (default is True).

    Returns
    -------
        - `str`: The cleaned and renamed column name.

    Example
    -------
    Apply the function to `new_infos` dataframe

    ```
    new_info.columns = new_info.columns.map(format_column_header)
    ```
    """
    # Replace non-alphanumeric characters with underscores
    sanitized = re.sub(r"[^a-zA-Z0-9]", "_", label)

    # Remove duplicate underscores and trailing underscores
    sanitized = re.sub(r"_+", "_", sanitized).strip("_")

    if lowercase:
        return sanitized.lower()
    else:
        return sanitized.upper()
