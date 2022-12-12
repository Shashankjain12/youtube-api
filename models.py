from mongoengine import Document, StringField, DateTimeField, URLField
from datetime import datetime


class Video(Document):
    vid_id = StringField(unique=True)
    title = StringField()
    description = StringField()
    published_date = DateTimeField("publishing datetime")
    created_date = DateTimeField(default=datetime.utcnow())
    thumbnail_url = URLField()
    vid_url = URLField()