# Dataframes

Provides methods to quickly adjust dataframes.

> [!NOTE]
> ```py
> from quati.data.processing import <FUNCTION>
> ```

- [`convert_magnitude_string()`](data.md#convert_magnitude_string): Transforms string-based magnitude suffixes (K, M, B) into numerical integers
- [`format_column_header()`](data.md#format_column_header): Normalizes DataFrame column names by handling special characters and casing

---

### `convert_magnitude_string()`
The `convert_magnitude_string()` function converts string-based number values (like "1K" or "10.3M") into their corresponding numerical values. It’s useful for normalizing data inputs with suffixes like "K" for thousand, "M" for million, etc.

```py
In  [1]: convert_magnitude_string("1K")
Out [1]: 1000

In  [2]: convert_magnitude_string("550.1K")
Out [2]: 550100

In  [3]: convert_magnitude_string("10.3M")
Out [3]: 10300000
```

### `format_column_header()`
The `format_column_header()` function renames DataFrame columns using a standardized normalization logic. It removes accents, replaces special characters with underscores, and enforces lowercase, ensuring consistent column naming across different sources.

```py
In  [1]: 
    Col_A    Cól-B_    cOl__C    col_d
0       3        ar        zz       11
1      12        tg        aa       22

In  [2]: df.columns = [format_column_header(c) for c in df.columns]
Out [2]: 
    col_a    col_b    col_c    col_d
0       3       ar       zz       11
1      12       tg       aa       22
```