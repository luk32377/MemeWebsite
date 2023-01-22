#!/usr/bin/python3

from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__,static_url_path="/static")

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/request", methods=["GET"])
def request():
	data = requests.get("https://meme-api.com/gimme/wholesomememes")
	dataurl = data.json()["url"]
	print(dataurl)
	return dataurl
	
if __name__ == "__main__":
	app.run(debug=True)
