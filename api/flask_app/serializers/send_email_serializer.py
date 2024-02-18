from flask_restx import reqparse, fields, inputs
from api.restplus import api

send_email_serializer = api.parser()

# add argument required in API
send_email_serializer.add_argument("type", type= str, required = True)
send_email_serializer.add_argument("company_name", type= str, required = True)
send_email_serializer.add_argument("sender_name", type= str, required = True)

send_email_response_model = api.model("SEND_EMAIL_RESPONSE", {
    "success": fields.String(),
    "message": fields.String()
})