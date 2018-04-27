from app import app, logic
from flask import request


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/addbook',methods=['POST'])
def addBook():
	return logic.addNewBook(request.json)


@app.route('/getbooklist', methods=['GET'])
def viewBookList():
	return logic.getBookList()

@app.route('/deletebook', methods=['POST'])
def deleteBook():
	return logic.removeBook(request.json)

'''
@app.route('/changeTag', methods=['PATCH'])
def changeTag():

@app.route('/viewbookswithfilter',methods=['GET'])
def viewBookWithFilter():

'''