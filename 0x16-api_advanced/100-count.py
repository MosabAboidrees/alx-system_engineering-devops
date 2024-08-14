#!/usr/bin/python3
""" Reddit API module to count occurrences of words in hot post titles """

import requests
import json


def count_words(subreddit, word_list, after="", word_count=[]):
    """
    Recursively counts the occurrences of each word in word_list
    in the titles of hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of words to count in the post titles.
        after (str): The 'after' parameter for Reddit API pagination.
        word_count (list): A list to store the count of each word.

    Returns:
        None: Prints the word counts directly.
    """

    # Initialize word_count on the first call
    if after == "":
        word_count = [0] * len(word_list)

    # Construct the URL for the subreddit's hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Send the GET request to the Reddit API
    response = requests.get(url,
                            params={'after': after},
                            allow_redirects=False,
                            headers={'User-Agent': 'bhalut'})

    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

        # Iterate through each post title
        for post in (data['data']['children']):
            title_words = post['data']['title'].split()
            for word in title_words:
                for i in range(len(word_list)):
                    # Increment count if word matches, case-insensitively
                    if word_list[i].lower() == word.lower():
                        word_count[i] += 1

        # Get the 'after' value for pagination
        after = data['data']['after']

        if after is None:
            # Handle duplicates and sort the results
            duplicates = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        duplicates.append(j)
                        word_count[i] += word_count[j]

            # Sort the words by count and alphabetically
            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (word_count[j] > word_count[i] or
                            (word_list[i]() > word_list[j]() and
                             word_count[j] == word_count[i])):
                        word_count[i], word_count[j] =\
                            word_count[j], word_count[i]
                        word_list[i], word_list[j] = word_list[j], word_list[i]

            # Print the results, excluding duplicates
            for i in range(len(word_list)):
                if (word_count[i] > 0) and i not in duplicates:
                    print("{}: {}".format(word_list[i].lower(), word_count[i]))
        else:
            # Recursively call the function to process the next page of results
            count_words(subreddit, word_list, after, word_count)
