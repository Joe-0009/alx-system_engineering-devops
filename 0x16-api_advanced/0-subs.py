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
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
