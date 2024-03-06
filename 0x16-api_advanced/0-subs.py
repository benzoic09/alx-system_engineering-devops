#!/usr/bin/python3
"""Module for task 0"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""

    # Construct the URL for subreddit information
    sub_info_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set custom User-Agent header
    headers = {"User-Agent": "Ubuntu 20.04"}

    # Make the GET request to the subreddit information URL
    response = requests.get(
        sub_info_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
