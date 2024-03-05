#!/usr/bin/python3

import requests 

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirect=False)

    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers
