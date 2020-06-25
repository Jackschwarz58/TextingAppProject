
from twilio.rest import Client
import config

client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

# Sends a messages to the specified recipient with text defined by the message_text param
# recipient: formatted phone number to which the message will be sent
# `message_text`: message text, since we are on the trial version this will be prefixed with "Sent from your Twilio trial account"


def send_message(recipient, message_text):
    message = client.messages \
        .create(
            body=message_text,
            messaging_service_sid=config.TWILIO_SERVICE_SID,
            to=recipient,
            # status_callback=config.POSTBIN_TEST
            # Test callback to postbin for review, REPLACE LATER
        )
    print(message.sid)  # Prints SID to confirm message sent


send_message('this is a test push',
             'Text back anything')
