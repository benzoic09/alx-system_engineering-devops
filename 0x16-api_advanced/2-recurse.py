#!/usr/bin/python3
""" task 2 """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive function that queries the Reddit
    API and returns a list of titles"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return None

    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        hot_list.append(child.get("data").get("title"))

    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
