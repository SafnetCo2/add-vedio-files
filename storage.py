import json
from pathlib import Path
from models import Video, Comment

DATA_FILE = Path("data.json")

def save_data(videos):
    data = [v.summary() for v in videos.values()]
    DATA_FILE.write_text(json.dumps(data, indent=2))

def load_data():
    if not DATA_FILE.exists():
        return {}
    raw_data = json.loads(DATA_FILE.read_text())
    videos = {}
    for v in raw_data:
        video = Video(v["id"], v["title"], v["uploader"], v["created_at"])
        for c in v.get("comments", []):
            comment = Comment(c["id"], c["author"], c["text"], c["likes"], c["created_at"])
            video.add_comment(comment)
        videos[video.id] = video
    return videos
