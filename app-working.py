import sys

from flask import Flask, render_template, request, redirect, Response
import json

app = Flask(__name__)

@app.route("/")
def output():
    return render_template("index-working.html")


# http://www.makeuseof.com/tag/python-javascript-communicate-json/

@app.route('/receiver', methods = ['POST'])
def worker():	
	print "==================================================="
	# read json + reply
	data = request.get_json()
	result = ''

	if data == None:
		print "data = none ouch"

	for item in data:
		# loop over every row
		print ">>>" + item['username']
		result += str(item['username']) + '\n'
	
	item['username'] = "PORKYPIES"
	print item['username']
	return result

if __name__ == "__main__":
    app.run()
