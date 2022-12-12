import os
from datetime import datetime, timedelta


env = os.environ.get("FAM_CONFIG", "prod")

BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
# Youtube API related stuff
query = "python"
max_results = 10
date = (datetime.now() - timedelta(seconds=30)).isoformat() + "Z"
