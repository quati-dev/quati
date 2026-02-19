# Web Scrapping

Provides a set of tools for automating browser interactions, allowing you to perform web scraping tasks with minimal code.

> [!NOTE]
> ```py
> from quati.navigation.automation import <FUNCTION>
> ```

- [`launch_navigator()`](navigation.md#launch_navigator): Initializes a customized Chrome WebDriver instance
- [`save_session_cookies()`](navigation.md#save_session_cookies): Exports active browser session cookies to a local file
- [`load_session_cookies()`](navigation.md#load_session_cookies): Injects saved cookies into the browser to bypass authentication
- [`is_node_present()`](navigation.md#is_node_present): Validates the existence of a web element using XPath
- [`dismiss_popup()`](navigation.md#dismiss_popup): Automates popup closure via ESC key or targeted element clicks

---

### `launch_navigator()`
The `launch_navigator()` function initializes a Chrome browser instance using Selenium. This function is essential for beginning a web scraping session.

```py
In [1]: path = "path/to/chromedriver"

In [2]: url = "https://www.example.com"

In [3]: browser = launch_navigator(url, path, is_headless=True)
```

### `save_session_cookies()`
The `save_session_cookies()` function exports cookies from the browser to maintain session state, which is useful for accessing authenticated web pages without logging in repeatedly.

```py
In [1]: save_session_cookies("/home/computer/Desktop/google_cookies.pkl", driver)
```

### `load_session_cookies()`
The `load_session_cookies()` function imports cookies into the browser to maintain session state, which is useful for bypassing login screens using previously saved sessions.

```py
In [1]: load_session_cookies("/home/computer/Desktop/", "cookieFile.pkl", driver)
```

### `is_node_present()`
The `is_node_present()` function checks if an element exists on a web page based on the provided XPath. This is useful for verifying the presence of elements before interacting with them.

```py
In  [1]: is_node_present(xpath_query="/html/body/div[1]/main/div[1]/svg")
Out [1]: True
```

### `dismiss_popup()`
The `dismiss_popup()` function either presses the ESC key or clicks on a specified element on a web page, depending on the action required. This is useful for closing intrusive pop-ups or handling dynamic overlays.

```py
In [1]: dismiss_popup(target_xpath="//div[@id='modal']", use_esc=True)

In [2]: dismiss_popup(target_xpath="//div[@id='modal']", element_css_class="close-btn")
```