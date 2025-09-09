# Web Scrapping

Provides a set of tools for automating browser interactions, allowing you to perform web scraping tasks with minimal code.

> [!NOTE]
> ```py
> from quati.scrapping.selenium import <FUNCTION>
> ```

- [`start_browser()`](scrapping.md#start_browser): Initialize a Chrome browser using Selenium
- [`export_cookies()`](scrapping.md#export_cookies): Export cookies from browser
- [`import_cookies()`](scrapping.md#import_cookies): Import cookies to browser
- [`check_element()`](scrapping.md#check_element): Function to check if an element exists on a web page based on the provided XPath
- [`esc_or_click()`](scrapping.md#esc_or_click): Function to either press the ESC key or click on an element on a web page

---

### `start_browser()`
The `start_browser()` function initializes a Chrome browser instance using Selenium. This function is essential for beginning a web scraping session.

```py
In [1]: path = "path/to/chromedriver"
In [1]: url = "https://www.example.com"
In [1]: browser = start_browser(path, url, headless=True)
```

### `export_cookies()`
The `export_cookies()` function exports cookies from browser to maintain session state, which is useful for accessing authenticated web pages without logging in repeatedly.

```py
In [1]: export_cookies("/home/computer/Desktop/", "cookieFile.pkl", driver)
```

### `import_cookies()`
The `import_cookies()` function imports cookies into the browser to maintain session state, which is useful for accessing authenticated web pages without logging in repeatedly.

```py
In [1]: import_cookies("/home/computer/Desktop/", "cookieFile.pkl", driver)
```

### `check_element()`
The `check_element()` function checks if an element exists on a web page based on the provided XPath. This is useful for verifying the presence of elements before interacting with them.

```py
In  [1]: check_element(driver, element_xpath="/html/body/div[1]/main/div[1]/svg"):
Out [1]: True
```

### `esc_or_click()`
The `esc_or_click()` function either presses the ESC key or clicks on a specified element on a web page, depending on the action required. This can be useful for closing pop-ups or interacting with elements dynamically.

```py
In [1]: esc_or_click(driver, esc=True)

In [1]: esc_or_click(driver, click_on_xpath="/html/body/div[1]/main/div[1]/svg")
```