from flask import render_template, request
from app import app
from app.utils import process_youtube_url

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        summary = process_youtube_url(youtube_url)
    return render_template('index.html', summary=summary)
