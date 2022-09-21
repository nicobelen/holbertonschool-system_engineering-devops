#!/usr/bin/python3
"""Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""


import requests


def top_ten(subreddit):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    try:
        n = 0
        r = requests.get('https://www.reddit.com/r/{}/hot.json'
                         .format(subreddit), headers=user_agent,
                         allow_redirects=False)
        children = r.json()['data']['children']
        for post in children:
            if (n < 10):
                print(post['data']['title'])
            n += 1
    except Exception:
        print(None)
