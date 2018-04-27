from app import database
from flask import jsonify
def addNewBook(raw_data):
	book = {"name":raw_data["name"], "author":raw_data["author"]}
	
	if database.checkBookExisted(book["name"]):
		return "Inser Fail!\n"
	else:
		database.insertOneBook(book)
		return "insert success!\n"

def getBookList():
	books = database.getAllBooks()
	books_list = [book["name"] for book in books]
	return jsonify(books_list)

def removeBook(raw_data):
	book = {"name":raw_data["name"], "author":raw_data["author"]}
	if database.checkBookExisted(book["name"]):
		database.deleteOneBook(book)
		return "Delete success!\n"
	else:
		return "Book does not exit!\n"