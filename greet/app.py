from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
	"""Returns string 'welcome'"""
	return 'welcome'

@app.route('/welcome/home')
def welcome_home():
	"""Returns string 'welcome home'"""
	return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
	"""Returns string 'welcome back'"""
	return 'welcome back'