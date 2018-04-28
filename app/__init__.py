from flask import Flask

app = Flask(__name__)

from app import requesthandler
app.config['UPLOAD_FOLDER'] = "./booksstorage"
