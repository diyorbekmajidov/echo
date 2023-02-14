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
    data = print(request.get_json(force=True))

    return 'ok'
