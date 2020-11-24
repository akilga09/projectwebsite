from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    video_test = FileField('Video', validators=[
        FileRequired(),
        FileAllowed(['mp4', 'mp3', 'Videos Only!'])
    ])
