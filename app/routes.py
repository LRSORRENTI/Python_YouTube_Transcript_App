from flask import render_template, request, jsonify
from app import app
from app.utils import process_youtube_url

def format_transcript(transcript, line_length=20, lines_per_paragraph=4):
    words = transcript.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 > line_length:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word) + 1
    
    if current_line:
        lines.append(' '.join(current_line))
    
    # Insert paragraph breaks every `lines_per_paragraph` lines
    formatted_lines = []
    for i in range(0, len(lines), lines_per_paragraph):
        formatted_lines.extend(lines[i:i + lines_per_paragraph])
        formatted_lines.append('')  # Add an empty line for paragraph break
    
    return '\n'.join(formatted_lines)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        summary = process_youtube_url(youtube_url)
    return render_template('index.html', summary=summary)

@app.route('/save_transcript', methods=['POST'])
def save_transcript():
    data = request.get_json()
    filename = data.get('filename')
    transcript = data.get('transcript')
    if filename and transcript:
        try:
            formatted_transcript = format_transcript(transcript, line_length=50, lines_per_paragraph=4)
            with open(filename, 'w') as file:
                file.write(formatted_transcript)
            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    return jsonify({'success': False, 'error': 'Invalid data'})
