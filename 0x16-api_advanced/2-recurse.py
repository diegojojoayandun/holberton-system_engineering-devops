#!/usr/bin/python3
"""  function that queries the Reddit API;
and print ten titles """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ return list of title """
    header = {'User-Agent': 'my_user_agent'}
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    try:
        response = requests.get(url, headers=header,
                                allow_redirects=False).json().get("data")
        after = response.get("after", None)
        for children in response.get("children"):
            hot_list.append(children.get("data").get("title"))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    except Exception:
        return(None)
