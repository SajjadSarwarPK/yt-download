from flask import Flask, request, jsonify
from pytubefix import YouTube
from po_token import main

app = Flask(__name__)

# Get YouTube video link
@app.route('/get_youtube_video_link', methods=['GET'])
def get_youtube_video_link():
    name_filter = request.args.get('video_link')

    if not name_filter:
        return jsonify({'error': 'video_link parameter is required'}), 400

    try:
        main()
        # Get the URL of the YouTube video
        yt = YouTube(name_filter, token_file='token.json')

        # Download the video
        video = yt.streams.get_highest_resolution()
        video_title = video.title
        video_url = video.url

        items = {'video_title': video_title, 'video_url': video_url}
        return jsonify(items), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
