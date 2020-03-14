from flask import Flask, request, jsonify, render_template
import datetime
import os
import requests
import json
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

@app.route('/')
def index():
    return ('Flask app running. But it is not bug free.')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)   # get the incoming JSON structure
    action = data['queryResult']['action'] # get the action name associated with the matched intent
    
    reply = {}
    response = ""
    
    if (action == 'test_connection'):
       response = "Reply from webhook: I've received your test connection. Good job. 👍"
    else:
       response = "Reply from webhook: I am not sure what to do  😟 😟 "
        
    reply["fulfillmentText"] = response
    return jsonify(reply)
    