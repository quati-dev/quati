import glob
import pickle
import platform
import warnings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

warnings.filterwarnings("ignore")


def launch_navigator(
    target_url: str = "about:blank",
    is_headless: bool = False,
    is_muted: bool = True,
    custom_flags: list[str] | None = None,
) -> webdriver.Chrome:

    chrome_cfg = webdriver.ChromeOptions()

    if is_headless:
        chrome_cfg.add_argument("--headless=new")

    if is_muted:
        chrome_cfg.add_argument("--mute-audio")

    flags = [
        "--allow-insecure-localhost",
        "--disable-blink-features=AutomationControlled",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--disable-gpu",
        "--disable-infobars",
        "--disable-setuid-sandbox",
        "--disable-web-security",
        "--ignore-certificate-errors",
        "--no-sandbox",
        "--remote-debugging-port=9222",
        "--start-maximized",
        "--window-size=1920,1080",
    ]

    if custom_flags:
        flags.extend(custom_flags)

    for flag in flags:
        chrome_cfg.add_argument(flag)

    driver = webdriver.Chrome(options=chrome_cfg)

    driver.get(target_url)

    return driver


def load_session_cookies(dir_path, search_term, driver_obj):
    """Import cookies to browser.

    Parameters
    ----------
    `dir_path` : Full file path.
    `search_term` : Full file_name or is prefix.
    `driver_obj` : Browser object

    Examples
    --------
    Implement cookie file to bypass login

    >>> load_session_cookies("/home/computer/Desktop/", "cookieFile", driver)
    >>> load_session_cookies("/home/computer/Desktop/", "cookieFile.pkl", driver)
    """
    try:
        match = glob.glob(f"{dir_path}*{search_term}*")
        if not match:
            return False
        cookie_file_path = str(match[0])
    except Exception:
        return False

    with open(cookie_file_path, "rb") as input_file:
        cookie_data = pickle.load(input_file)

    for data in cookie_data:
        driver_obj.add_cookie(data)

    return driver_obj


def save_session_cookies(destination_path, driver_obj):
    """
    Export cookies from the current browser session to a file.

    Parameters
    ----------
    `driver_obj` : Browser object
        The Selenium WebDriver instance with an active session.
    `destination_path` : str
        Full path (including filename) where the cookies will be saved.

    Returns
    -------
    bool
        True if cookies were successfully saved, False otherwise.

    Example
    -------
    >>> save_session_cookies(browser, "/home/user/Desktop/google_cookies.pkl")
    """
    try:
        session_cookies = driver_obj.get_cookies()
        with open(destination_path, "wb") as output_file:
            pickle.dump(session_cookies, output_file)
        return True
    except Exception as error:
        print(f"Cookie export failed: {str(error)}")
        return False


def is_node_present(xpath_query: str = ""):
    """
    Function to check if an element exists on a web page based on the provided XPath.

    Args:
        xpath_query (str): XPath expression to locate the element on the web page.

    Returns:
        bool: True if the element is found, False otherwise.
    """
    try:
        # Assumes 'browser' is defined globally or managed in scope
        browser.find_element(By.XPATH, xpath_query)
        return True
    except Exception:
        return False


def dismiss_popup(target_xpath: str, use_esc: bool = False, element_css_class: str = ""):
    """
    Function to either press the ESC key or click on an element on a web page.

    Args:
        target_xpath (str): XPath expression to locate the element to ignore.
        use_esc (bool): If True, press the ESC key. Defaults to False.
        element_css_class (str): Class name to locate the element to click on. Defaults to an empty string.

    Returns:
        None
    """
    attempts = 0
    while is_node_present(target_xpath) and attempts < 3:
        if use_esc:
            # Send escape key signal
            webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
        else:
            # Locate by partial class match and click
            browser.find_element(By.XPATH, f"//*[contains(@class, '{element_css_class}')]").click()

        # 'pls_wait' is assumed to be a sleep wrapper defined elsewhere
        import time

        time.sleep(5)
        attempts += 1
