from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/videostream')
def stream():
    return render_template('videostream.html')


@app.route('/videos')
def videos():
    return render_template('videos.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
