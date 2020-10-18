from flask import Flask, request, make_response, jsonify
import random
# from image_search import ImageSearch
import json
import pprint

app = Flask(__name__)
# driver = "/usr/bin/chromedriver"
# driver = "../chromedriver"
# ims = ImageSearch(driver, headless=True)
@app.route("/")
def index():
	return "Get data"

@app.route("/data", methods=["POST"])
def data():
	q = request.json["num"]
	n = int(random.random() * 100)
	# q = request.json["query"]
	# d = json.dumps(ims.search(q))
	return jsonify({"n": n, "answer ": q + n})

