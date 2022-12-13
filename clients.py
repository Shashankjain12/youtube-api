import os
from datetime import datetime, timedelta


red_server = os.environ.get("RED_SERVER", "localhost")
red_port = os.environ.get("RED_PORT", 6380)
MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)
API_KEY = os.environ.get("API_KEY")

BROKER_URL = f"redis://{red_server}:{red_port}/0"
CELERY_RESULT_BACKEND = f"redis://{red_server}:{red_port}/1"
# Youtube API related stuff
query = "python"
max_results = 10
date = (datetime.now() - timedelta(minutes=30)).isoformat() + "Z"
