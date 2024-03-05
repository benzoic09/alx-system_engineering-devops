#!/usr/bin/python3
"""task one"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and returns the top 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        print(None)

