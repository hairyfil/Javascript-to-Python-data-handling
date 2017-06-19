import sys

from flask import Flask, render_template, request, redirect, Response
import json

app = Flask(__name__)

@app.route("/")
def output():
    return render_template("index.html")


# http://www.makeuseof.com/tag/python-javascript-communicate-json/

@app.route('/receiver', methods = ['POST'])
def worker():	
	print "==================================================="
	# read json + reply
	data = request.get_json()

	if data == None:
		print "********** data = none ouch ************ "

	print data

	for item in data:
		# loop over every row
		username 		= item['username']
		fingerprint 	= item['fingerprint']
		mydevice 		= item['mydevice']
		mydevicetype 	= item['mydevicetype']
		mydevicevendor 	= item['mydevicevendor']
		browser 		= item['browser']
		browserversion 	= item['browserversion']
		opsys 			= item['opsys']
		opsysversion 	= item['opsysversion']


	print
	print "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
	print "Username = " + username 
	print "fingerprint = " + fingerprint
	print "Device  = " + mydevice
	print "Device Type = " + mydevicetype
	print "Device Vendor = " + mydevicevendor
	print "Operating System = " + opsys + "   [Verion: " + opsysversion + "]"
	print "Browser = " + browser + "   [Version: " + browserversion + "]"
	print "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
	print

	return ""

if __name__ == "__main__":
    app.run()
