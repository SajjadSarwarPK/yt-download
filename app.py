from flask import Flask, request, jsonify
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable  # Import specific exceptions if needed

app = Flask(__name__)


# Get YouTube video link
@app.route('/get_youtube_video_link', methods=['GET'])
def get_youtube_video_link():
    name_filter = request.args.get('video_link')

    if not name_filter:
        return jsonify({'error': 'video_link parameter is required'}), 400

    try:
        # Get the URL of the YouTube video
        yt = YouTube(name_filter)

        # Download the video
        video = yt.streams.get_highest_resolution()
        video_title = video.title
        video_url = video.url

        items = {'video_title': video_title, 'video_url': video_url}
        return jsonify(items), 200

    except VideoUnavailable:
        return jsonify({'error': 'The video is unavailable.'}), 404
    except Exception as e:
        return jsonify({'error': str(e), "yt":str(yt)}), 500


if __name__ == '__main__':
    app.run(debug=True)
