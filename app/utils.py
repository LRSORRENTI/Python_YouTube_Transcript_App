# from pytube import YouTube
# from moviepy.editor import AudioFileClip
# import speech_recognition as sr
# from transformers import pipeline
# import os
# import tempfile

# def process_youtube_url(youtube_url):
#     try:
#         yt = YouTube(youtube_url)
#         video = yt.streams.filter(only_audio=True).first()
#         temp_dir = tempfile.mkdtemp()
#         audio_path = video.download(output_path=temp_dir)

#         # Extract audio from video
#         audio_clip = AudioFileClip(audio_path)
#         audio_file_path = os.path.join(temp_dir, "audio.wav")
#         audio_clip.write_audiofile(audio_file_path)
#         audio_clip.close()

#         # Transcribe audio to text
#         recognizer = sr.Recognizer()
#         with sr.AudioFile(audio_file_path) as source:
#             audio = recognizer.record(source)
#             try:
#                 text = recognizer.recognize_google(audio)
#             except sr.RequestError as e:
#                 return f"Could not request results from Google Web Speech API; {e}"
#             except sr.UnknownValueError:
#                 return "Google Web Speech API could not understand the audio"

#         # Summarize the transcribed text
#         summarizer = pipeline("summarization")
#         summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

#         # Clean up temporary files
#         os.remove(audio_path)
#         os.remove(audio_file_path)
#         os.rmdir(temp_dir)

#         return summary
#     except Exception as e:
#         return f"An error occurred: {str(e)}"

# TRANSCRIPT VERSION 
import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

def chunk_text(text, max_length, tokenizer):
    """Splits the text into chunks of max_length tokens."""
    tokens = tokenizer.encode(text, truncation=False)
    chunks = []
    for i in range(0, len(tokens), max_length):
        chunk = tokens[i:i + max_length]
        chunks.append(tokenizer.decode(chunk, skip_special_tokens=True))
    return chunks

def summarize_text(text, summarizer, max_length=1024, min_length=30):
    """Summarizes text using the provided summarizer pipeline."""
    summaries = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return ' '.join([summary['summary_text'] for summary in summaries])

def process_youtube_url(youtube_url):
    try:
        # Extract video ID from the YouTube URL
        video_id = youtube_url.split('v=')[-1].split('&')[0]

        # Fetch the transcript
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([item['text'] for item in transcript_list])
        print(transcript_text)
        return transcript_text
    except Exception as e:
        return f"An error occurred: {str(e)}"
