from models import Video
from connection import Connection
import json

def paginated_extractor(page_no):
    """
    Extracts in a descending order of the publishing date
    """
    items_per_page = 5

    offset = (page_no + 1) * items_per_page
    with Connection():
        vid_list = Video.objects.order_by('published_date').skip(offset).limit(items_per_page)
        vid_list = json.loads(vid_list.to_json())
        # for i in vid_list:
        #     print(i['published_date']["$date"])

    return vid_list

def text_search(text):
    """
    Extracts the docs based on the texts
    """
    with Connection():
        # vids_titles = Video.objects({"$text":{"$search":title}})
        vids_texts = Video.objects.search_text(text)
        vids_texts = json.loads(vids_texts.to_json())
    return vids_texts