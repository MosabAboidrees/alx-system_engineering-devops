#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    # Validate the subreddit argument
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    # Set up the User-Agent header to mimic a browser request
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

    # Limit the response to the first 10 hot posts
    params = {'limit': 10}

    # Construct the URL for the subreddit's hot posts
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    # Send the GET request to the Reddit API
    response = get(url, headers=headers, params=params)

    # Parse the JSON response
    subreddit_data = response.json()

    try:
        # Extract the list of hot posts from the response data
        posts = subreddit_data.get('data').get('children')

        # Loop through the posts and print each title
        for post in posts:
            print(post.get('data').get('title'))

    except Exception:
        # Print "None" if an error occurs during the request or parsing process
        print("None")
