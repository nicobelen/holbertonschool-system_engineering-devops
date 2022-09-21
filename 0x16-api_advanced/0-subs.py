#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0."""


import requests


def number_of_subscribers(subreddit):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    try:
        r = requests.get('https://www.reddit.com/r/{}/about.json'
                         .format(subreddit), headers=user_agent)
        return r.json()['data']['subscribers']
    except Exception:
        return 0
