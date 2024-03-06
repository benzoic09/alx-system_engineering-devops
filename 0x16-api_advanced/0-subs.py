#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    sub_info_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(
        sub_info_url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data", {}).get("subscribers", 0)
