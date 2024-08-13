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
    # Validate the subreddit_name argument
    if not subreddit or not isinstance(subreddit, str):
        return 0

    # Define the User-Agent header to mimic a browser request
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    # Construct the URL to access the subreddit's about.json data
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send the GET request to the Reddit API
    response = get(url, headers=headers)

    # Parse the JSON response
    subreddit_data = response.json()
    try:
        # Return the number of subscribers, or 0 if the key is not found
        return subreddit_data.get('data', {}).get('subscribers', 0)

    except Exception:
        # Return 0 if any error occurs during the request or parsing process
        return 0
