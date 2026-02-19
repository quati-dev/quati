import mimetypes
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

# Asset and Connection Settings
BRAND_LOGO_LINK = "https://raw.githubusercontent.com/quati-dev/quati/refs/heads/main/assets/quati.png"
MAIL_SERVER = "smtp.mailing.com"
MAIL_PORT = 587

# Visual Themes for Alerts
ALERT_THEMES = {
    "error": {"primary": "#E63946", "glyph": "🔴", "alias": "Critical Error"},
    "important": {"primary": "#8338EC", "glyph": "🔥", "alias": "Priority"},
    "note": {"primary": "#3A86FF", "glyph": "📝", "alias": "Information"},
    "tip": {"primary": "#06D6A0", "glyph": "✨", "alias": "Insight"},
    "warning": {"primary": "#FFBE0B", "glyph": "🔸", "alias": "Warning"},
}


class Dispatcher:
    """
    Class for sending alert emails with custom HTML and attachment support.

    Allows you to configure a sender user, authentication token, and default recipient list.
    Uses SMTP with STARTTLS for secure sending.

    Args
    ----
    - `account_user` (str): Sender's email address.
    - `access_key` (str): Sender's app token or password (e.g., Gmail).
    - `default_list` (list[str]): Default recipient list

    Example
    -------
    ```
        notifier = Dispatcher("sys@service.com", "key_123", ["admin@service.com"])
        notifier.push_emsg(title="Failure", message="System down", type="error")
    ```
    """

    def __init__(self, account_user: str, access_key: str, default_list: list[str]):
        self.sender_id = account_user
        self.secret = access_key
        self.mailing_list = default_list

    def push_emsg(
        self,
        abstract: str = "N/A",
        title: str = "System Notification",
        datetime: str = "Unknown Time",
        message: str = "Empty Body",
        context: str = "General",
        extra_data: dict = None,
        files: list[str] = [],
        type: str = "error",
        recipients: list[str] = None,
    ):
        if type not in ALERT_THEMES:
            raise ValueError(f"Category '{type}' is not supported. Choose from {list(ALERT_THEMES.keys())}")

        # Extract Theme Config
        ui = ALERT_THEMES[type]
        accent, icon, tag = ui["primary"], ui["glyph"], ui["alias"]
        email_subject = f"System Notification • [{tag.upper()}] {title}"

        # Dynamic Metadata Generation
        custom_fields = ""
        if extra_data:
            for key, val in extra_data.items():
                custom_fields += f"<div style='margin-bottom: 4px;'><b>{key}:</b> {val}</div>"

        # Refined Modern Template
        email_content = f"""<!DOCTYPE html>
<html>
<head>
    <style>
        .canvas {{ 
            background-color: #f4f7f6; 
            padding: 50px 20px; 
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; 
        }}
        .paper {{ 
            max-width: 550px; 
            margin: 0 auto; 
            background: #ffffff; 
            border-radius: 20px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
            padding: 40px; 
        }}
        .badge {{ 
            display: inline-block; 
            background: {accent}15; 
            color: {accent}; 
            padding: 6px 14px; 
            border-radius: 50px; 
            font-size: 11px; 
            font-weight: 700; 
            text-transform: uppercase; 
            letter-spacing: 1px; 
            margin-bottom: 20px; 
        }}
        .headline {{ 
            font-size: 22px; 
            color: #1a1a1a; 
            margin: 0 0 15px 0; 
            font-weight: 600; 
        }}
        .txt {{ 
            color: #525252; 
            font-size: 15px; 
            line-height: 1.7; 
            margin-bottom: 25px;
        }}
        .bubble {{ 
            background: #fdfdfd; 
            border: 1px dashed #e0e0e0; 
            padding: 20px; 
            border-radius: 12px; 
            margin: 25px 0; 
            color: #444; 
            font-size: 14px;
        }}
        .info-grid {{ 
            font-size: 13px; 
            color: #888; 
            border-top: 1px solid #eee; 
            margin-top: 30px; 
            padding-top: 20px; 
            line-height: 1.8;
        }}
        .footer {{ 
            text-align: center; 
            font-size: 12px; 
            color: #b0b0b0; 
            margin-top: 30px; 
        }}
    </style>
</head>
<body>
    <div class="canvas">
        <div style="text-align: center; margin-bottom: 25px;">
            <img src="cid:brand_logo" width="80" style="opacity: 0.8;">
        </div>
        <div class="paper">
            <span class="badge">{icon} {title}</span>
            <h1 class="headline">A new automated update has arrived:</h1>
            <p class="txt">{abstract}</p>
            
            <div class="bubble">
                <strong style="font-size: 11px; color: #999; display: block; margin-bottom: 8px; letter-spacing: 0.5px;">ADDITIONAL DETAILS:</strong>
                {message}
            </div>
            <div class="info-grid">
                <div><b>Date and time:</b> {datetime}</div>
                <div><b>Context:</b> {context}</div>
                {custom_fields}
            </div>
        </div>
        <div class="footer">
            Sent via <b>Quati</b><br>
            This is an automated system notification.
        </div>
    </div>
</body>
</html>"""

        # Construct Email Object
        container = MIMEMultipart("related")
        container["Subject"] = email_subject
        container["From"] = self.sender_id
        container["To"] = ", ".join(recipients or self.mailing_list)
        container.attach(MIMEText(email_content, "html"))

        # Embed Brand Logo
        try:
            raw_img = requests.get(BRAND_LOGO_LINK).content
            img_attachment = MIMEBase("image", "png")
            img_attachment.set_payload(raw_img)
            encoders.encode_base64(img_attachment)
            img_attachment.add_header("Content-ID", "<brand_logo>")
            img_attachment.add_header("Content-Disposition", "inline", filename="logo.png")
            container.attach(img_attachment)
        except Exception as e:
            print(f"Warning: Could not embed logo: {e}")

        # Process File Attachments
        for path in files:
            kind, _ = mimetypes.guess_type(path)
            kind = kind or "application/octet-stream"
            major, minor = kind.split("/", 1)

            with open(path, "rb") as source_file:
                payload = MIMEBase(major, minor)
                payload.set_payload(source_file.read())
                encoders.encode_base64(payload)
                payload.add_header("Content-Disposition", f"attachment; filename={path.split('/')[-1]}")
                container.attach(payload)

        # Transmission Logic
        with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
            server.starttls()
            server.login(self.sender_id, self.secret)
            server.sendmail(self.sender_id, recipients or self.mailing_list, container.as_string().encode("utf-8"))
