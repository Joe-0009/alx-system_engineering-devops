#!/usr/bin/python3
'''
    This module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        Prints the titles of the first 10 hot posts for a given subreddit
    '''
    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/yourusername)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        try:
            for post in data.get('data').get('children'):
                print(post.get('data').get('title'))
        except Exception:
            print(None)
    else:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
