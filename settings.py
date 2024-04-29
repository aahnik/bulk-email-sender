import os

from dotenv import load_dotenv

load_dotenv()

DISPLAY_NAME = os.getenv("display_name")
SENDER_EMAIL = os.getenv("sender_email")
PASSWORD = os.getenv("password")
MAIL_COMPOSE: str = os.getenv("mail_compose", "compose.md")
SUBJECT: str | None = os.getenv("subject", None)

try:
    assert DISPLAY_NAME
    assert SENDER_EMAIL
    assert PASSWORD
    assert MAIL_COMPOSE
except AssertionError:
    print("Please set up credentials. Read https://github.com/aahnik/automailer#usage")
else:
    print("Credentials loaded successfully")

    print(DISPLAY_NAME)
    print(SENDER_EMAIL)
    print(PASSWORD)
    print(SUBJECT)
