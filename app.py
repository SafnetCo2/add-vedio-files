from flask import Flask, jsonify, request, render_template, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'


# --- Helper functions for saving/loading data ---
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


# --- Load existing data ---
videos = load_data()


# --- Routes ---

@app.route('/')
def home():
    return render_template('index.html', videos=videos)


# CREATE
@app.route('/videos', methods=['POST'])
def add_video():
    data = request.form
    video = {
        'id': len(videos) + 1,
        'title': data.get('title'),
        'author': data.get('author'),
        'comments': []
    }
    videos.append(video)
    save_data(videos)
    return redirect(url_for('home'))


# UPDATE
@app.route('/videos/<int:video_id>/update', methods=['POST'])
def update_video(video_id):
    video = next((v for v in videos if v['id'] == video_id), None)
    if not video:
        return jsonify({'error': 'Video not found'}), 404

    data = request.form
    video['title'] = data.get('title', video['title'])
    video['author'] = data.get('author', video['author'])
    save_data(videos)
    return redirect(url_for('home'))


# DELETE
@app.route('/videos/<int:video_id>/delete', methods=['POST'])
def delete_video(video_id):
    global videos
    videos = [v for v in videos if v['id'] != video_id]
    save_data(videos)
    return redirect(url_for('home'))


# ADD COMMENT
@app.route('/videos/<int:video_id>/comments', methods=['POST'])
def add_comment(video_id):
    video = next((v for v in videos if v['id'] == video_id), None)
    if not video:
        return jsonify({'error': 'Video not found'}), 404

    data = request.form
    comment = {
        'user': data.get('user'),
        'text': data.get('text')
    }
    video['comments'].append(comment)
    save_data(videos)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
