from pymongo import MongoClient
client = MongoClient('localhost',27017)
bookdb = client.database_1
book_collection = bookdb.collection_1

def insertOneBook(book):
	book_collection.insert_one(book)

def checkBookExisted(name):
    return book_collection.find_one({"name":name})

def getAllBooks():
	return book_collection.find()

def deleteOneBook(book):
	book_collection.delete_one(book)

def changeBookTags(name,tags):
	book_collection.update_one({"name":name}, {"$set":{"tags":tags}}, upsert=True)

def getBooksWithFilter(book_filter,limit):
	if limit > 0:
		return book_collection.find(book_filter).limit(limit)
	else:
		return book_collection.find(book_filter)


