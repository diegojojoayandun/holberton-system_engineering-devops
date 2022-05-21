#!/usr/bin/python3
""" Modules to get the number of subscribers from a Reddit subreddit." """


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    If an invalid subreddit is given, the function should return 0.
    """

    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    options = {'allow_redirects': False}

    try:
        response = requests.get(url=url,
                                headers=headers,
                                allow_redirects=options,)

        return response.json().get("data").get("subscribers")
    except Exception:
        return 0
