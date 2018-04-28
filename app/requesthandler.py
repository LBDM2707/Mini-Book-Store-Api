from app import app, logic
from flask import request


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/addbook',methods=['POST'])
def addBook():
	return logic.addNewBook(request)


@app.route('/getbooklist', methods=['GET'])
def viewBookList():
	return logic.getBookList()

@app.route('/deletebook', methods=['POST'])
def deleteBook():
	return logic.removeBook(request)


@app.route('/changetag', methods=['POST'])
def changeTag():
	return logic.updateBookTags(request)


@app.route('/getbookslistwithfilter',methods=['GET'])
def viewBookWithFilter():
	return logic.getBookListByFilter(request)
