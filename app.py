from flask import Flask
from tasks import search_youtube
app = Flask(__name__)


@app.route("/async_youtube")
def youtube_search():
    search_youtube.delay()
    return "Youtube Async initiated", 200



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")