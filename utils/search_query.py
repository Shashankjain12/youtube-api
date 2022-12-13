# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
from clients import max_results, date, API_KEY
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def search_query(query):
    # Fetching from YT source
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    # Order by date query as song max results as 10 and published Before 30 seconds from query
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=max_results,
        order="date",
        publishedAfter=date
    )
    response = request.execute()

    return response
