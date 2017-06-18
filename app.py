import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route("/output")
def output():
    return render_template("index.html", name="Joe")

# http://www.makeuseof.com/tag/python-javascript-communicate-json/

@app.route('/receiver', methods = ['POST'])
def worker():	
	# read json + reply
	data = request.get_json()
	result = ''

	if data == None:
		print "data = none ouch"

	for item in data:
		# loop over every row
		result += str(item['make']) + '\n'

	return result

if __name__ == "__main__":
    app.run()
