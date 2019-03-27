import os
import urllib.parse

from flask import Flask, request, Response, jsonify, redirect
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

STRAVA_CLIENT_ID = os.environ.get('STRAVA_CLIENT_ID')
STRAVA_CLIENT_SECRET = os.environ.get('STRAVA_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')

def exchange_token(code):
    strava_request = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': STRAVA_CLIENT_ID,
            'client_secret': STRAVA_CLIENT_SECRET,
            'code': code,
            'grant_type': 'authorization_code'
        }
    )
    return jsonify(strava_request.json())

@app.route('/strava_authorize', methods=['GET'])
def strava_authorize():
    params = {
        'client_id': STRAVA_CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': 'activity:read_all'
    }
    return redirect('{}?{}'.format(
        'https://www.strava.com/oauth/authorize',
        urllib.parse.urlencode(params)
    ))

@app.route('/strava_token', methods=['GET'])
def strava_token():
    code = request.args.get('code')
    if not code:
        return Response('Error: Missing code param', status=400)
    return exchange_token(code)
