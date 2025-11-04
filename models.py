from abc import ABC, abstractmethod
from datetime import datetime

class Identifiable(ABC):
    """Abstract base showing abstraction."""
    def __init__(self, id):
        self._id = id
        self._created_at = datetime.utcnow()

    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at

    @abstractmethod
    def summary(self):
        pass


class Comment(Identifiable):
    def __init__(self, id, author, text, likes=0):
        super().__init__(id)
        self.author = author
        self.text = text
        self.likes = likes

    def like(self):
        self.likes += 1

    def summary(self):
        return {
            "id": self.id,
            "author": self.author,
            "text": self.text,
            "likes": self.likes,
            "created_at": self.created_at.isoformat()
        }


class Video(Identifiable):
    def __init__(self, id, title, uploader):
        super().__init__(id)
        self.title = title
        self.uploader = uploader
        self.comments = []

    def add_comment(self, comment):
        if not isinstance(comment, Comment):
            raise TypeError("Expected Comment instance")
        self.comments.append(comment)

    def summary(self):
        return {
            "id": self.id,
            "title": self.title,
            "uploader": self.uploader,
            "total_comments": len(self.comments),
            "comments": [c.summary() for c in self.comments],
            "created_at": self.created_at.isoformat()
        }
from datetime import datetime

class Comment:
    def __init__(self, id, author, text, likes=0, created_at=None):
        self.id = id
        self.author = author
        self.text = text
        self.likes = likes
        self.created_at = created_at or datetime.utcnow().isoformat()

    def summary(self):
        return {
            "id": self.id,
            "author": self.author,
            "text": self.text,
            "likes": self.likes,
            "created_at": self.created_at
        }

class Video:
    def __init__(self, id, title, uploader, created_at=None):
        self.id = id
        self.title = title
        self.uploader = uploader
        self.comments = []
        self.created_at = created_at or datetime.utcnow().isoformat()

    def add_comment(self, comment):
        self.comments.append(comment)

    def summary(self):
        return {
            "id": self.id,
            "title": self.title,
            "uploader": self.uploader,
            "comments": [c.summary() for c in self.comments],
            "created_at": self.created_at
        }
