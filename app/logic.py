from app import database
from flask import jsonify
from app import bookhandler




def addNewBook(request):
	book = bookhandler.constructBook(request)
	if database.checkBookExisted(book["name"]):
		return "Inser Fail!\n"
	else:
		database.insertOneBook(book)
		return "insert success!\n"

def getBookList():
	books = database.getAllBooks()
	books_list = [book["name"] for book in books]
	return jsonify(books_list)

def removeBook(request):
	book = bookhandler.constructBook(request)

	if database.checkBookExisted(book["name"]):
		database.deleteOneBook(book)
		return "Delete success!\n"
	else:
		return "Book does not exit!\n"

def updateBookTags(request):
	if database.checkBookExisted(request.form["name"]) and request.form["tags"]:
		tags = request.form["tags"]
		tags = [tag.lower() for tag in tags]
		database.changeBookTags(request.form["name"], tags)
		return "Update tags success!\n"
	else:
		return "No tag found!\n"


def getBookListByFilter(request):
	book_filter = bookhandler.constructBookFilters(request)
	books_limit = 0
	if "limit" in request.form and request.form["limit"].isdigit():
		books_limit = int(request.form["limit"])
	books = database.getBooksWithFilter(book_filter,books_limit)
	books_list =[book["name"] for book in books]
	return jsonify(books_list)