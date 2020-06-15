from twilio.rest import Client
import config

client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

message = client.messages \
    .create(
        body="Texting, Texting. 1, 2, 3. Is this thing on?",
        messaging_service_sid ='MGd36eca31a7f5b39044832032b917db63',
        to='+14054712092',
        status_callback='https://postb.in/1592252035200-6130564089398'
    )

print(message.sid)