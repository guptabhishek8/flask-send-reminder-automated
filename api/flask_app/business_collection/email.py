import logging

import smtplib
from email.message import EmailMessage
from email.utils import formataddr

from ..constants import common_constants
from ..constants.third_party_constants import OUTLOOK_EMAIL_SERVICE
from settings import OUTLOOK_SENDER_EMAIL, OUTLOOK_PASSWORD_EMAIL

# logging setup
logger = logging.getLogger("flask_app")

HTTPCODES = common_constants.HTTPCODES


def send_email(subject, receiverEmail, receiverName, dueDate, amount, message, senderName,reminderType, companyName):

    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = formataddr((f"{companyName}", f"{OUTLOOK_SENDER_EMAIL}"))
        msg["To"] = receiverEmail
        msg["BCC"] = OUTLOOK_SENDER_EMAIL

        msg.set_content(
            f"""\
            Hi {receiverName},
            I hope you are well.
            I just wanted to drop you a quick note to remind you that Rs. {amount} in respect of {reminderType} is due for payment on {dueDate}.
            I would be really grateful if you could confirm that everything is on track for payment. 
            Best Regards,
            {senderName}
            """)
        
        # Adding the Html version. This converts the message into a multipart/alternative
        msg.add_alternative(
            f"""\
            <html>
                <body>
                    <p>Hi {receiverName}, </p>
                    <p>I hope you are well. </p>
                    <p>I just wanted to drop you a quick note to remind you that <strong> Rs. {amount} </strong>in respect of {reminderType} is due for payment on <strong>{dueDate} </strong></p>
                    <p>I would be really grateful if you could confirm that everything is on track for payment.</p>
                    <p>Best Regards</p>
                    <p> {senderName}</p>
                </body>
            </html>
            """,
            subtype = "html",
        )

        print(f"Sending Email Reminder to {receiverName}:{receiverEmail}: {msg.as_string()}")

        with smtplib.SMTP(OUTLOOK_EMAIL_SERVICE.get("SERVER"), OUTLOOK_EMAIL_SERVICE.get("PORT")) as server:
            server.starttls()
            server.login(OUTLOOK_SENDER_EMAIL, OUTLOOK_PASSWORD_EMAIL)
            server.sendmail(OUTLOOK_SENDER_EMAIL, receiverEmail, msg.as_string())

        print(f"Succesfully Sent Email Reminder to {receiverEmail}")
        return HTTPCODES.get("SUCCESS")
            
    except Exception as error:
        print(f"Error Occured while sending email reminder  {receiverName}:{receiverEmail}, error: {error}")
        return HTTPCODES.get("INTERNAL_SERVER_ERROR")





# def first_app(input):

#     # Input your Logic here 
#     print(f"First Logic")
#     response = s3.get_object(Bucket=bucket_name, Key=path)
#     return returnData