from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from parse import handleReponse
# from helper import load_user_list
# from sender import send_message

app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def incoming_sms():
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print(request.values)
    resp = handleReponse(body, request)

    return str(resp)


@ app.route("/")
def home():
    return "Flask is up and running!"


if __name__ == "__main__":
    app.run(debug=True)
