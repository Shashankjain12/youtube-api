from flask import Flask
from tasks import search_youtube
from utils.mongod import paginated_extractor, text_search
app = Flask(__name__)


@app.route("/ping")
def ping():
    return "Pinged the server", 200

@app.route("/async_youtube")
def youtube_search():
    search_youtube.delay()
    return "Youtube Async initiated", 200

@app.route("/search/<int:page_no>")
def search_vid(page_no):
    """
    Searches from youtubedb in a paginated fashion
    """
    videos_list = paginated_extractor(page_no=page_no)
    return videos_list, 200

@app.route("/search_text/<string:text>")
def search_by_text(text):
    """
    Searches from youtubedb using text
    """
    videos_list = text_search(text)
    return videos_list, 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")