# Messengers & Alerts

Provides a class to send styled alerts and informational emails from just a few lines of code.

> [!NOTE]
> ```py
> from quati.msger.mailing import Dispatcher
> ```

- [`Dispatcher`](#dispatcher-class): Class to send HTML alert emails (types: error, tip, note, important, warning) with detailed context, attachments and metadata.
- [`push_emsg()`](#push_emsg-method): Method of `Dispatcher` to trigger the actual sending of the email.

---

### `Dispatcher` class

The `Dispatcher` class allows you to configure a sender (`account_user`, `access_key`) and default recipients. It sends a rich HTML-formatted alert email with metadata, attachments, and styling based on the selected theme.

#### Initialize email sender
```py
notifier = Dispatcher(
    account_user="your_email@gmail.com",
    access_key="your_app_token",
    default_list=["team@example.com", "devops@example.com"]
)
```

### `push_emsg()` method
The `push_emsg()` method sends a formatted alert email based on the provided type (`error`, `important`, `note`, `tip`, or `warning`), including optional metadata and attachments.

#### Parameters:
- `abstract` (`str`): Short summary of the alert
- `title` (`str`): Email subject/title
- `datetime` (`str`): When the event occurred
- `message` (`str`): Detailed log or traceback
- `context` (`str`): Name of the process or module
- `extra_data` (`dict`, optional): Key-value pairs shown in the email
- `files` (`list[str]`, optional): List of file paths to attach
- `type` (`str`): One of error, tip, note, important, warning
- `recipients` (`list[str]`, optional): Override recipient list

```py
notifier.push_emsg(
    abstract="Daily Reminder",
    title="Friendly Notice",
    datetime="2026-02-18 23:40",
    message="Just a quick reminder about your scheduled activity.",
    context="personal",
    extra_data={"Category": "Routine", "Importance": "Normal"},
    files=['./local_img.png'],
    type="info",
)
```