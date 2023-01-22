#!/usr/bin/python3

from flask import Flask, request, render_template
import requests
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__,static_url_path="/static")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/request", methods=["GET"])
#@cross_origin()
def request():
	data = requests.get("https://meme-api.com/gimme/wholesomememes")
	dataurl = data.json()["url"]
	print(dataurl)
	return dataurl
	
@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response
	
if __name__ == "__main__":
	app.run()
