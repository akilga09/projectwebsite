from flask import Flask

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'
UPLOAD_FOLDER = 'static/videos'
SAVED_FOLDER = 'static/videos2'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config.from_object(__name__)

allowed_uploads = ['mp4', 'mp3']

from app import views
