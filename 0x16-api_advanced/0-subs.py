#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    # Check if subreddit is a valid string
    if not isinstance(subreddit, str):
        return 0

    # Construct the URL for subreddit information
    sub_info_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set custom User-Agent header
    headers = {"User-Agent": "CustomClient/1.0"}

    # Make the GET request to the subreddit information URL
    response = requests.get(
        sub_info_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data and "subscribers" in data:
            return data["subscribers"]
    return 0
