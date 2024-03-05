#!/usr/bin/python3
""" task 2 """

from json import loads
from requests import get


def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API and returns a list
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    
    headers = {'User-Agent': "Custom User Agent"}
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for title in children:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    except:
        print(None)
        return 0
