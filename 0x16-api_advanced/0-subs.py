#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
to return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    the function returns 0.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if subreddit is invalid.
    """
    # URL of the subreddit's about.json
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # User-Agent header is needed to avoid 429 status code (Too Many Requests)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;\
               x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                   Chrome/127.0.0.0 Safari/537.36 Edg/127.0.2651.98'}

    # allow_redirects=False to avoid redirection to the search page
    response = requests.get(url, headers=headers, allow_redirects=False)
    # 200 is the status code for a successful HTTP request
    if response.status_code == 200:
        # returns the JSON data of the response
        data = response.json()
        # returns the number of subscribers
        return data.get('data', {}).get('subscribers', 0)
    else:  # if the status code is not 200
        return 0  # return 0
