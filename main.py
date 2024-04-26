from flask import Flask, render_template, request, send_file, Response
from pytube import YouTube
import os

app = Flask(__name__, static_url_path='', static_folder='templates')

def download_video(url, path):
    try:
        youtube = YouTube(url)
        video = youtube.streams.filter(only_audio=True).first()
        video.download(path)
        for file in os.listdir(path):
            if file.endswith(".mp4"):
                video_file = os.path.join(path, file)
                if not os.path.isfile(video_file):
                    print(f"Warning: Video file '{video_file}' not found.")
                    continue
                os.rename(video_file, os.path.join(path, get_filename(url)))
        return True
    except Exception as e:
        print("Error occurred:", e)
        return False

def get_filename(url):
    """Extract the filename from the given YouTube URL."""
    youtube = YouTube(url)
    video = youtube.streams.filter(only_audio=True).first()
    return video.default_filename

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    path = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(path):
        os.makedirs(path)
    download_successful = download_video(url, path)
    if download_successful:
        filename = get_filename(url)
        filepath = os.path.join(path, filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            return "Error: Downloaded file not found"
    else:
        return "Error: Download Failed"


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
