from twilio.twiml.messaging_response import MessagingResponse


def handleReponse(body, request):
    print('BODY TEXT: \'' + body+'\'')
    # Start our TwiML response

    messageText = ''
    resp = MessagingResponse()

    bodyContent = body.lower()

    # Determine the right reply for this message
    if 'commands' in bodyContent:
        messageText += createHelpResponse()
    elif 'no' in bodyContent:
        messageText += "Oh, Sorry about that!"
    elif 'yes' in bodyContent:
        messageText += "Okay! I\'ll get right on that."
    elif 'test' in bodyContent:
        messageText += str(request.values.to_dict)
    else:
        messageText += 'Sorry, I didn\'t catch that. What was that again? (This command may not be implemented yet)'

    resp.message(messageText)
    return resp


def createHelpResponse():
    helpResponse = ""

    helpResponse += "Currently, I am able to recognize the following Keywords:\nyes, no, commands, test"

    return helpResponse
