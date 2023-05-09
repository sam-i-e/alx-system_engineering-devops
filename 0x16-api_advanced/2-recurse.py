#!/usr/bin/python3
"""
This function queries a list of all hot posts on a given subreddit on Reddit.
"""

import os
import requests


def recurse(subreddit, hot_list=[], after="", len_list=0):
    '''
    Recursively lists all files in a directory
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {
            'after': after,
            'limit': 100,
            'count': len_list
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for child in children:
            result = child['data']['title']
            hot_list.append(result)
        after = data['data']['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after, len(hot_list))
