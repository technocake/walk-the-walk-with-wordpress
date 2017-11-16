# coding: utf-8
import hashlib

from flask import Flask
app = Flask(__name__)

@app.route('/')
def ninjas():
	
	def gravatarurl(email):
		emailhash = hashlib.md5(email.lower()).hexdigest()
		size = 50
		url = "https://www.gravatar.com/avatar/%s?s=%d" %(
			emailhash,
			size
		)
		return url

	return "<img src='%s' />" % gravatarurl(b'robin.aaberg@knowit.no')
