#!/usr/bin/python3
"""This is a function that queries subscribers on a given subreddit on Reddit."""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit Api"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        no_subs = data["data"]["subscribers"]
        return no_subs
    else:
        return 0
