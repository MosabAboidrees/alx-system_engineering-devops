#!/usr/bin/python3
"""
Module to interact with Reddit's API to retrieve hot post titles recursively.
"""

import requests

# Global variable to track the 'after' parameter for pagination
after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the titles of all hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot posts.

    Returns:
        list: A list containing the titles of hot posts,
        or None if an error occurs.
    """

    # Use the global 'after' variable to keep track of pagination
    global after

    # Set up the User-Agent header to identify
    # the script making the API request
    headers = {'User-Agent': 'api_advanced-project'}

    # Construct the URL for the subreddit's hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set the parameters for the request, including pagination with 'after'
    params = {'after': after}

    # Send the GET request to the Reddit API
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the 'after' value for pagination
        after_data = response.json().get("data").get("after")

        # If there is more data to retrieve, update 'after' and recurse
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)

        # Extract the list of posts from the response data
        posts = response.json().get("data").get("children")

        # Append each post title to the hot_list
        for post in posts:
            hot_list.append(post.get("data").get("title"))

        return hot_list
    else:
        # Return None if an error occurs during the request
        return None

