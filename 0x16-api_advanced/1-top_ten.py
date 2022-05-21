#!/usr/bin/python3
"""
Modules to get the  the titles of the first 10 hot posts
listed for Reddit subreddit."
"""


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """

    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    options = {'allow_redirects': False}

    try:
        response = requests.get(url=url,
                                headers=headers,
                                allow_redirects=options)

        for _item in response.json().get('data').get('children'):
            print(_item.get('data').get('title'))

    except Exception:
        return None
