from api.restplus import api
from flask_restx import Resource
from flask import request
from ..business_collection.reminder_sheets import loan_reminder_sheet
from ..serializers.send_email_serializer import send_email_serializer, send_email_response_model
from ..serializers.common_serializer import bad_request_response, unauthorized_response
from ...auth import requires_auth
from settings import LOAN_REMINDER_SHEET_ID, LOAN_REMINDER_SHEET_NAME



import logging

logger = logging.getLogger("flask_app")

email_ns  = api.namespace('email-api', description = 'calling from email-api')

@email_ns.route('/sendEmail')
class ClassName(Resource):

    @requires_auth
    @api.expect(send_email_serializer, validate = True)
    @api.marshal_with(send_email_response_model, skip_none = True)
    @api.doc(responses = {401: ("Unautorized access", unauthorized_response),
                          400: ("Bad Request", bad_request_response)
                          })
    def post(self):

        body = send_email_serializer.parse_args()
        if body.get("type") == "loan":
            companyName = body.get("company_name")
            senderName = body.get("sender_name")
            status, message = loan_reminder_sheet(LOAN_REMINDER_SHEET_ID, LOAN_REMINDER_SHEET_NAME, companyName, senderName)
        else:
            status = "SUCCESS"
            message = "Type provided in body: not supported"

        return {"success":status, "message": message}
