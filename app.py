from flask import Flask, request
import requests
import os

# flask app
app = Flask(__name__)

# TOKEN
TOKEN = os.environ['TOKEN']


@app.route('/webhook', methods=['POST'])
def webhook():
    # get data from request
    update = print(request.get_json(force=True))
    text = update['message']['text']
    chat_id = update['message']['chat']['id']
    # send message
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    r = requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params=payload)

    return 'ok'
