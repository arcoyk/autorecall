from flask import Flask, request, make_response, jsonify
# from image_search import ImageSearch
import json

app = Flask(__name__)
# driver = "/usr/bin/chromedriver"
# driver = "../chromedriver"
# ims = ImageSearch(driver, headless=True)
@app.route("/", methods=["GET"])
def index():
	return "Access /data by POST to get data"

@app.route("/data", methods=["POST"])
def index():
	r = make_response(jsonify({"hoge":43, "fuga": "ga"}), 200)
	# q = request.json["query"]
	# d = json.dumps(ims.search(q))
	return r
