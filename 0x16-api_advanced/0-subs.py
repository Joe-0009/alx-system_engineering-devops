#!/usr/bin/python3
"""
Queries the Reddit API
returns the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    return the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get('data')
    return result.get("subscribers")
