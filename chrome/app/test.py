from flask import Flask, request
from image_search import ImageSearch
import json

app = Flask(__name__)
driver = "/usr/bin/chromedriver"
# driver = "../chromedriver"
ims = ImageSearch(driver, headless=True)

@app.route("/", methods=["POST"])
def index():
	q = request.json["query"]
	d = json.dumps(ims.search(q))
	return d
