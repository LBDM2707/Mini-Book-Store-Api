# Mini-Book-Store-Api

Prequisite:
	Python3
	Flask
	MongoDB

Running:
$ export FLASK_APP=bookstore.py
$ flask run



Insert book:
curl -X POST localhost:5000/addbook -H "Content-Type: multipart/form-data" -F name=book1 -F author=book2 -F file_data=@./demo1.py

Get book list:
curl -X GET http://localhost:5000/getbooklist

Delete a book:
curl -X POST localhost:5000/deletebook -H "Content-Type: multipart/form-data" -F name=book1 

Change tag for book:
curl -X POST localhost:5000/changetag -H "Content-Type: multipart/form-data" -F name=book1 -F tag=[tag1,tag2,tag3]

Get book list with filter
curl -X POST localhost:5000/getbookslistwithfilter -H "Content-Type: multipart/form-data" -F [options] 

	options: name=[bookname] (use regex to find books)
			 tags=[tags list] (find book that have all tags in the list)
			 limit=[number of result] (limit the number of returning result)