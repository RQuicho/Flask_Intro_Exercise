# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
	"""Adds two numbers when typed in URL.
	>>> localhost:5000/add?a=2&b=3
	2 + 3 = 5
	"""
	a = int(request.args["a"])
	b = int(request.args["b"])
	ans = add(a, b)
	return f"{a} + {b} = {ans}"

@app.route('/sub')
def sub_nums():
	"""Subtracts two numbers when typed in URL
	>>> localhost:5000/sub?a=5&b=2
	5 - 2 = 3
	"""
	a = int(request.args["a"])
	b = int(request.args["b"])
	ans = sub(a, b)
	return f"{a} - {b} = {ans}"

@app.route('/mult')
def mult_nums():
	"""Multiply two numbers when typed in URL
	>>> localhost:5000/mult?a=7&b=9
	7 * 9 = 63
	"""
	a = int(request.args["a"])
	b = int(request.args["b"])
	ans = mult(a, b)
	return f"{a} * {b} = {ans}"

@app.route('/div')
def div_nums():
	"""Divide two numbers when typed in URL
	>>> localhost:5000/mult?a=10&b=2
	10 / 2 = 5
	"""
	a = int(request.args["a"])
	b = int(request.args["b"])
	ans = div(a, b)
	return f"{a} / {b} = {ans}"
	


