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

expired_keys = []

def search_query(query, pageToken=""):
    # Fetching from YT source
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    global expired_keys
    
    api_service_name = "youtube"
    api_version = "v3"
    key = None
    
    # Get credentials and create an API client
    # Handling the expiring of API keys
    for api_key in API_KEY:
        if api_key not in expired_keys:
            key = api_key
            youtube = googleapiclient.discovery.build(
                api_service_name, api_version, developerKey=api_key, cache_discovery=False)
    
    if not key:
        print("No keys are present for Yotube Search")
        # Raise an alert
        return None
    
    search_results = True
    # Order by date query as song max results as 10 and published Before 30 seconds from query
    data = []
    while search_results:
        try:
            request = youtube.search().list(
                q=query,
                part="snippet",
                maxResults=max_results,
                order="date",
                publishedAfter=date,
                pageToken=pageToken if pageToken != "" else ""
            )
            response = request.execute()
            pageToken = response.get('nextPageToken')
            if not response.get("items", []) or not pageToken:
                search_results = False
                break
            data.extend(response.get("items", []))
        except Exception as e:
            # Expired keys handler
            search_results = False
            expired_keys.append(key)
            print(f"Key has been expired with error {e}")
            
    return data
