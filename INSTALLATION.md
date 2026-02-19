# Installation

## Python version support

Officially `Python 3.10`.

## Setup Steps

1. **Create a local virtual environment:**

    ```sh
    python3.10 -m venv .venv
    ```

2. **Activate the virtual environment:**

    Close the terminal and reopen it. This will help ensure the virtual environment is activated correctly. If you are using `VS Code`, it may ask if you want to change the runtime to the newly created one.

    *If the environment is not automatically activated, use the following command:*

   - Linux, macOS:
       ```sh
       source .venv/bin/activate
       ```
   - Windows:
       ```cmd
       .venv\Scripts\activate
       ```

3. **Install the required libraries:**
    ```sh
    pip install -r requirements.txt
    ```

4. **The directory is ready to use.**

<hr>

### Additional Notes

- To deactivate the virtual environment, you can use the command:
    ```sh
    deactivate
    ```
- Every time you open the project in `VS Code`, it will be automatically identified and initialized.
- Make sure all dependencies are listed in the [`requirements.txt`](requirements.txt) file to ensure the environment is configured correctly.

<hr>

[⇧ Go to Top](#table-of-contents)