from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
# from helper import load_user_list
# from sender import send_message

app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def incoming_sms():
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print(body)
    print(str(request.data))

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body.lower() == 'yes':
        msg = resp.message("Wow! You Replied Yes")
    elif body.lower() == 'no':
        msg = resp.message("Shit! You Replied No")
    else:
        msg = resp.message(
            'You really don\'t like following directions huh? Try again smartass')

    msg.media('https://i.imgur.com/FbIRYFr.png')

    return str(resp)


@ app.route("/")
def home():
    return "Flask is up and running!"


if __name__ == "__main__":
    app.run(debug=True)
