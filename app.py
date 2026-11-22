import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv('APP_VERSION', 'dev')

@app.get('/')
def index():
    return jsonify(message='hello saas', version=VERSION)

@app.get('/healthz')
def healthz():
    return 'okokokok'
