from mongoengine import connect
from clients import MONGO_HOST, MONGO_PORT

class Connection:
    def __enter__(self):
        self.conn = connect('youtubedb', host=MONGO_HOST, port=int(MONGO_PORT))
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
