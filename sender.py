from twilio.rest import Client
import config

client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

## Sends a messages to the specified recipient with text defined by the message_text param
## recipient: formatted phone number to which the message will be sent
## `message_text`: message text, since we are on the trial version this will be prefixed with "Sent from your Twilio trial account"
def send_message(recipient, message_text):
    message = client.messages \
        .create(
            body= message_text,
            messaging_service_sid ='MGd36eca31a7f5b39044832032b917db63',
            to= recipient,
            status_callback='https://postb.in/1592252035200-6130564089398' # Test callback to postbin for review, REPLACE LATER
        )
    print(message.sid) # Prints SID to confirm message sent

