from flask import Flask, request, jsonify
from pytubefix import YouTube
from typing import Tuple

app = Flask(__name__)


def my_po_token_verifier() -> Tuple[str, str]:
    return (
        'CgtBLWxOdHFNQlREOCimh5W5BjIKCgJQSxIEGgAgEQ%3D%3D',
        'MnQL5bEHXyF1vwvd1h5tz6AxqWqTG7FSe02d3L0N13elCwpd7x5FOsk95Si7Hx2uZ9V0MTAaTLG9UdFwnrgylT-OLBqXemfHfviIhhHI4P-9O57B01CSOwEGgkqmwANJEl9BplTUZKCvLKwIzJE8z-Z3huwPyA=='
    )

# Get YouTube video link
@app.route('/get_youtube_video_link', methods=['GET'])
def get_youtube_video_link():
    name_filter = request.args.get('video_link')

    if not name_filter:
        return jsonify({'error': 'video_link parameter is required'}), 400

    try:
        # run_script()
        # Get the URL of the YouTube video
        yt = YouTube(name_filter, use_po_token=True, po_token_verifier=my_po_token_verifier, allow_oauth_cache=False)

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
