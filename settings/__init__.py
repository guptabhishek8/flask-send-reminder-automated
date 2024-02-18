import logging
import os
import sys
import dotenv

DEBUG = True
# ENV = "prod"
# APP_ENV = os.environ.get("APP_ENV", 'local')

dotenv.load_dotenv(os.getcwd() + '/.env')


BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")

OUTLOOK_SENDER_EMAIL = os.getenv("OUTLOOK_SENDER_EMAIL")
OUTLOOK_PASSWORD_EMAIL = os.getenv("OUTLOOK_PASSWORD_EMAIL")

LOAN_REMINDER_SHEET_ID = os.getenv("LOAN_REMINDER_SHEET_ID")
LOAN_REMINDER_SHEET_NAME = os.getenv("LOAN_REMINDER_SHEET_NAME")


# if APP_ENV == "prod":
#     dotenv.load_dotenv(os.getcwd() + '/.env')

#     GST_BUCKET_NAME = os.getenv("GST_BUCKET_NAME")
#     BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
#     BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")
    
#     # from .settings_production import *
# else:
#     try:
#         from .settings_local import *
#     except ImportError:
#         logging.error("No local settings detected. add settings/setting_local.py with local configuration setting")
#         sys.exit()