# Python YouTube Transcript App

## Overview

**The Python YouTube Transcript App is a web application that allows users to input a YouTube URL and retrieve the transcript of the video. The application is built using Flask for the backend and leverages the youtube-transcript-api library to fetch the transcript directly from YouTube. This app is useful for quickly obtaining the textual content of YouTube videos, which can be used for analysis, note-taking, or any other purpose.**

### Features
- User-Friendly Interface: Simple and intuitive form to input YouTube URLs.
- Transcript Retrieval: Fetches the full transcript of the YouTube video.
- Error Handling: Gracefully handles errors and provides meaningful feedback to users.

### Technologies Used
- Flask: A lightweight WSGI web application framework for Python.

- youtube-transcript-api: A library to retrieve transcripts from YouTube videos.

- HTML/CSS: For the frontend interface.

### Project Structure
```
youtube_transcript_app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   ├── templates/
│   │   ├── layout.html
│   │   ├── index.html
│   └── utils.py
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

### Setup and Installation

1. **Clone the Repository**

```
git clone https://github.com/yourusername/youtube_transcript_app.git

cd youtube_transcript_app

```
2. **Create a Virtual Environment** 

```
python -m venv venv
```
```
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install Dependencies**

```
pip install -r requirements.txt
```

4. **Run the Application**

```
python run.py
```

5. **Open the Application**

Open your web browser and navigate to http://127.0.0.1:5000/.

### Usage

- Input a YouTube URL: Enter the URL of the YouTube video you want to get the transcript for.

- Submit: Click the "Get Transcript" button.

- View Transcript: The transcript will be displayed on the page.

### License

This project is licensed under the MIT License. See the LICENSE file for details.