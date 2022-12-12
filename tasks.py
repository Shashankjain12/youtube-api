from celery import Celery
from utils.search_query import search_query
from clients import BROKER_URL
from models import Video
from dateutil import parser
from connection import Connection

task = Celery('tasks', broker=BROKER_URL)


@task.task(name='tasks.search_youtube')
def search_youtube():
    """
    Cron Job which will run every 30 seconds fetch vids
    from youtube using the gcloud api then push as a Document
    to MongoDB.
    """
    # Fetching the songs kind of data from YT
    resp = search_query(query="songs")
    with Connection():
        # With active connection from mongoengine
        for item in resp.get("items", []):
            # Extracts the items from the response
            vid_id = item["id"]["videoId"]
            # Extract by vid id if it exists then don't push the data again
            vid = Video.objects.filter(vid_id=vid_id).first()
            if not vid and item["id"]["kind"] == "youtube#video":
                snippet = item["snippet"]
                vid_url = f"https://www.youtube.com/watch?v={vid_id}"
                # Class Video Object for insertion into MongoDB
                video = Video(
                    vid_id=vid_id,
                    title=snippet["title"],
                    description=snippet["description"],
                    published_date=parser.parse(snippet["publishedAt"]),
                    thumbnail_url=snippet["thumbnails"]["default"]["url"],
                    vid_url=vid_url
                )
                video.save()
