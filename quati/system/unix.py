import os
import glob
import subprocess
import warnings
from datetime import datetime
from time import sleep
from tqdm import tqdm

warnings.filterwarnings("ignore")

BASE_PATH = "./"
PATH_PLACEHOLDER = BASE_PATH
SRC_IDENTIFIER = f"{BASE_PATH}filename.txt"
DEST_IDENTIFIER = f"{BASE_PATH}new_filename.txt"


def modify_file_name(
    folder_path=PATH_PLACEHOLDER,
    current_name=SRC_IDENTIFIER,
    updated_name=DEST_IDENTIFIER,
):
    """Rename a file.

    Parameters
    ----------
    `folder_path` : Full file path.
    `current_name` : Full filename or its prefix.
    `updated_name` : The new name to assign to this file

    Examples
    --------
    Rename a file called test.csv to newname.csv

    ```
    modify_file_name("/home/computer/Desktop/finalFolder", "test.csv", "newname.csv")
    ```
    """
    matches = glob.glob(os.path.join(folder_path, f"{current_name}*"))
    if matches:
        target_path = matches[0]
        new_path = os.path.join(folder_path, updated_name)
        os.rename(target_path, new_path)


def erase_file(folder_path=PATH_PLACEHOLDER, target_file=SRC_IDENTIFIER):
    """Delete a file.

    Parameters
    ----------
    `folder_path` : Full file path.
    `target_file` : Full filename or its prefix.

    Examples
    --------
    Delete a file called test.csv

    ```
    erase_file("/home/computer/Desktop/finalFolder", "test.csv")
    ```
    """
    full_path = os.path.join(folder_path, target_file)
    # Using os.remove for cross-platform safety over subprocess rm
    if os.path.exists(full_path):
        os.remove(full_path)


def locate_and_verify_file(
    folder_path=PATH_PLACEHOLDER,
    target_pattern=SRC_IDENTIFIER,
    byte_threshold=1,
    max_wait=15,
):
    """Checks the existence of a file, returning True or False.

    Parameters
    ----------
    `folder_path` : Full file path.
    `target_pattern` : Full filename or is prefix.
    `byte_threshold` : The minimum size of a file to be able to use it
    `max_wait` : Maximum waiting time to find the file

    By default:
        - `byte_threshold` : is considered 1
            - must be informed in bytes
        - `max_wait` : wait 15 seconds

    Examples
    --------
    Looking for a file that actually exists, called "teste.txt", with a minimum of 100 Bytes and waiting a maximum of 10 seconds

    ```
    locate_and_verify_file("/home/computer/Desktop/finalFolder", "test", 100, 10)
    True
    ```
    """
    is_ready = False
    deadline = int(datetime.now().timestamp()) + max_wait

    while not is_ready:
        try:
            found_items = glob.glob(os.path.join(folder_path, f"{target_pattern}*"))

            if found_items:
                target_item = found_items[0]
                if os.path.isfile(target_item):
                    actual_size = os.path.getsize(target_item)

                    if actual_size >= byte_threshold:
                        is_ready = True
                        return is_ready

            sleep(1)
            if int(datetime.now().timestamp()) >= deadline:
                return False
        except Exception:
            if int(datetime.now().timestamp()) >= deadline:
                return False


def display_timer(duration=1, use_visual: bool = True):
    """Shows a progress bar while waiting X seconds

    By default:
        - duration = 1

    ```
    display_timer(5)
    |======>    |100% 6/10s [08 Feb,2023 10:19:49<10:19:59]


    display_timer(5, use_visual=False)
    ```
    """
    label = f"Waiting {duration}s"
    if use_visual:
        for _ in tqdm(range(duration), desc=label):
            sleep(1)
    else:
        sleep(duration)


def fetch_host_details():
    """
    Retrieves system information using the 'uname -a' command.

    Returns:
        `dict`: A dictionary containing the system information with the following keys:
            - `kernel_name`: The name of the kernel.
            - `hostname`: The hostname of the system.
            - `kernel_version`: The version of the kernel.
            - `build_info`: Additional build information.
            - `architecture`: The system architecture.

    Raises:
        subprocess.CalledProcessError: If the 'uname -a' command fails to execute.

    ```
    info = fetch_host_details()
    print(info['hostname'])
    print(info['kernel_version'])
    ```
    """
    try:
        execution = subprocess.run(["uname", "-a"], capture_output=True, text=True, check=True)
        raw_string = execution.stdout.strip()
        segments = raw_string.split()

        data_map = {
            "kernel_name": segments[0],
            "hostname": segments[1],
            "kernel_version": segments[2],
            "build_info": " ".join(segments[3:6]),
            "architecture": " ".join(segments[6:]),
        }

        return data_map
    except Exception as err:
        print(f"Diagnostics failure: {err}")
        return None
