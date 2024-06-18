#!/usr/bin/python3
"""
 list containing tall he titles of all hot articles
 for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    if after:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                     after)
        headers = {'User-Agent': 'user agent 1.0'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            dt = response.json()
            posts = dt["data"]["children"]
            for post in posts:
                hot_list.append(post['data']['title'])

            after = dt["data"]["after"]
            return recurse(subreddit, hot_list, after)
        else:
            return None
    else:
        return hot_list
