import time
import os
from werkzeug.utils import secure_filename
from app import app
book_attributes = ["name", "author","tags"]


def constructBook(request):
	book = {}
	book_data = request.form.to_dict()
	
	for key in book_attributes:
		if key in book_data.keys():
			book[key] = book_data[key]
		else:
			book[key] = None
	book["upload_date"] = time.strftime('%A %B, %d %Y %H:%M:%S')
	if "file_data" in request.files:
		print("hello \n")
		file = request.files["file_data"]
		if file.filename != '':
			filename = secure_filename(file.filename)
			filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			open(filepath,"wb+")
			file.save(filepath)
			book["file"] = filepath
	return book

def constructBookFilters(request):
	filter_data = request.form.to_dict()
	filter={}
	if "name" in filter_data:
		filter["name"] = {"$regex":filter_data["name"], "$options":"i"}
	if "tags" in filter_data:
		filter["tag"] = {"$all":filter_data["tags"]}
	return filter


