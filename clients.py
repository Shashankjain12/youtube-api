import os

env = os.environ.get("FAM_CONFIG", "prod")

if env == "prod":
    BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
else:
    BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = None