from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from app.forms import UploadForm
from app import app, allowed_uploads
import os


# app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True

            flash('You were logged in', 'success')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/videostream', methods=['POST', 'GET'])
def stream():
    if not session.get('logged_in'):
        abort(401)

    return render_template('videostream.html')


@app.route('/home')
def home():
    if not session.get('logged_in'):
        abort(401)

    return render_template('index.html')


@app.route('/videos', methods=['POST', 'GET'])
def videos():
    if not session.get('logged_in'):
        abort(401)

        # Instantiate  form class
    video_upload = UploadForm()

    # Validate file upload on submit
    if request.method == 'POST':
        if video_upload.validate_on_submit():
            print(request.files['video_test'])
            app.logger.info('posted')
            # Get file data and save to your uploads folder
            videos = video_upload.video_test.data

        filename = secure_filename(videos.filename)
        videos.save(os.path.join(
            app.config['SAVED_FOLDER'], filename
        ))

        flash('Video Saved', 'success')
        return redirect(url_for('videos'))

    video_file_list = get_uploaded_videos()
    print(video_file_list)

    flash_errors(video_upload)
    return render_template('videos.html', form=video_upload, uploaded_videos=video_file_list)


@app.route('/contact')
def contact():
    if not session.get('logged_in'):
        abort(401)

    return render_template('contact.html')


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return redirect(url_for('login'))


def get_uploaded_videos():
    uploads = []
    for subdir, dirs, filer in os.walk(app.config['SAVED_FOLDER']):
        for file in filer:
            if file.split('.')[-1] in allowed_uploads:
                uploads.append(file)

    return uploads


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
