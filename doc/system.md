# System Utilities

Provides several methods to use system functionality from just a few lines of code.

> [!NOTE]
> ```py
> from quati.system.unix import <FUNCTION>
> ```

- ['erase_file()`](system.md#erase_file): Removes a specified file from the file system
- ['modify_file_name()`](system.md#modify_file_name): Renames an existing file based on path and prefix
- ['locate_and_verify_file()`](system.md#locate_and_verify_file): Searches for a file and validates it against a minimum size threshold
- ['display_timer()`](system.md#display_timer): Implements a wait period with an optional visual progress bar
- ['fetch_host_details()`](system.md#fetch_host_details): Extracts detailed system architecture and kernel information using the 'uname -a' command

---

### `erase_file()`
The 'erase_file()` function deletes a specified file from a given directory. This function is useful for removing files that are no longer needed.
```py
In  [1]: erase_file("tmp/finalFolder", "test.csv")
Out [1]: 

In  [2]: erase_file("system.xlsx")
Out [2]: 
```

### `modify_file_name()`
The 'modify_file_name()` function allows you to rename an existing file from its original name to a new name. It is useful for organizing files or correcting file names.
```py
In  [1]: modify_file_name("../Desktop/finalFolder", "test.csv", "newname.csv")
Out [1]: 
```

### `locate_and_verify_file()`
The 'locate_and_verify_file()` function searches for the existence of a file within a specified directory. It returns 'True' if the file is found and meets size requirements, or 'False' if it is not. You can set a minimum file size in *bytes* or specify a timeout in seconds.
```py
In  [1]: locate_and_verify_file("/home/computer/Desktop/finalFolder", "test", 100, 10)
Out [1]: True

In  [2]: locate_and_verify_file("test.json")
Out [2]: 
```

### `display_timer()`
The 'display_timer()` function pauses execution for a specified number of seconds. Optionally, a progress bar can be displayed via 'tqdm' to show the remaining time during the wait.
```py
In  [1]: display_timer(5)
Out [1]: Waiting 5s: 100%|██████████| 5/5 [00:05<00:00,  1.00s/it]

In  [2]: display_timer(5, False)
Out [2]: 
```

### `fetch_host_details()`
The 'fetch_host_details()` function retrieves detailed system information by executing the 'uname -a' command and parsing the result into a dictionary.
```py
In  [1]: 
    info = fetch_host_details()
    if info:
        print(info['kernel_name'])
        print(info['hostname'])
        print(info['kernel_version'])
        print(info['build_info'])
        print(info['architecture'])
Out [1]: 
    Linux
    device.hostname
    23.78.0-237.gtaV.x86_64
    #1 SMP PREEMPT_DYNAMIC Wed Jul 9 21:22:20 UTC 2021
    x86_64 x86_64 x86_64 GNU/Linux
```