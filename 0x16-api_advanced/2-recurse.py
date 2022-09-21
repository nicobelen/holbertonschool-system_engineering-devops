#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function should return None."""


import requests


def recurse(subreddit, hot_list=[], after=None):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json'
                         .format(subreddit), headers=user_agent,
                         params={'after': after}, allow_redirects=False)
        after = r.json()['data']['after']
        children = r.json()['data']['children']
        for post in children:
            hot_list.append(post['data']['title'])
        if (after is not None):
            recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
