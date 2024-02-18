import pandas as pd
from datetime import date
import logging
from ..constants import common_constants

from .email import send_email


logger = logging.getLogger("flask_app")
HTTPCODES = common_constants.HTTPCODES


def loan_reminder_sheet(sheetId, sheetName, companyName, senderName):
    try:
        subject  = "Loan Reminder"
        reminderType = "Loan"

        url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"

        dateFormat = ['due_date', 'reminder_date']

        df = pd.read_csv(url, parse_dates = dateFormat)

        present = date.today()
        emailCount = 0 
        for _, row in df.iterrows():
            if (present >= row['reminder_date'].date() and row['has_paid'] == "no"):
                send_email(
                    subject,
                    row['email'],
                    row['name'],
                    row['due_date'].strftime("%d, %b %Y"),
                    row["amount"],
                    "message",
                    senderName,
                    reminderType,
                    companyName
                )
                emailCount +=1

        message = f"Total No. of email sent: {emailCount}"

        return HTTPCODES.get("SUCCESS"),message
    
    except Exception as error:
        return HTTPCODES.get("INTERNAL_SERVER_ERROR"), error
        
    
