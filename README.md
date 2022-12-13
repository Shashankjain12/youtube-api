## Youtube Vid Scraper

This repository is maintained using Python Flask and Celery an Async based task Queue

### Tech Stack Used

Flask - Python Framework to build API for extracting the videos from Youtube.

MongoDB - MongoDB is being used as its easy to scale up and scale down without worrying much about
         definite schema or structure. We can also use shards in case load brings up.

Youtube API google api client - For extracting the videos from youtube

celery and celeryBeat - Celery an Async Task based queue is implemented in order to run the tasks in background
                        so that our api won't stop executing and Celery Beat a cron scheduler to run our Application in 30 sec intervals

Docker - For containerising my application

Docker-compose - for running multiple services parallely along with credentials

### API's exposed
1. async_youtube/ - For running the asynchronous tasks based queue on demand
2. search_text/{String:text} - To search relevant text based on the database a user facing service
3. search/<int:pg_number> - Paginated api which is based on the page number (max_results per page 5)

--------------------
Build the Application
--------------------


```
> pip install -r requirements.txt
> celery -A tasks worker --loglevel=INFO
> celery -A celery_cron beat --loglevel=INFO
> python3 app.py 

```

--------------------------
Composing the Docker file
---------------------------

```
> docker-compose up
```

