#!/usr/bin/python3
"""task one"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = response.json()  # Convert response to JSON

        if "data" in data and "children" in data["data"]:
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print(None)

# Example usage:
# top_ten("askreddit")
