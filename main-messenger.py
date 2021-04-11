import credentials
import requests
from flask import Flask, request
app = Flask(__name__)

# Adds support for GET requests to our webhook
@app.route('/webhook',methods=['GET'])
def webhook():
    verify_token = request.args.get("hub.verify_token")
    # Check if sent token is correct
    if verify_token == credentials.WEBHOOK_VERIFY_TOKEN:
        # Responds with the challenge token from the request
        return request.args.get("hub.challenge")
    return 'Unable to authorise.'

# Adds support for POST requests

@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.get_json()
    message = data['entry'][0]['messaging'][0]['message']
    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    if message['text']:
        request_body = {
                'recipient': {
                    'id': sender_id
                },
                'message': {"text":"hello, world!"}
            }
        response = requests.post('https://graph.facebook.com/v5.0/me/messages?access_token='+credentials.TOKEN,json=request_body).json()
        return response
    return 'ok'

if __name__ == "__main__":
    app.run(threaded=True, port=5000)