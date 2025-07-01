from flask import Flask, render_template, request
from utils.yt_api import get_video_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_data = None
    if request.method == 'POST':
        url = request.form.get('url')
        video_id = extract_video_id(url)
        if video_id:
            video_data = get_video_data(video_id)
    return render_template('index.html', video=video_data)

def extract_video_id(url):
    if 'v=' in url:
        return url.split('v=')[-1].split('&')[0]
    elif 'youtu.be/' in url:
        return url.split('youtu.be/')[-1].split('?')[0]
    return None

if __name__ == '__main__':
    app.run(debug=True)
