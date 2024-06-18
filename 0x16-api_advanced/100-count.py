#!/usr/bin/python3
"""
Module to count words in the titles of hot articles from a specified subreddit
"""
import requests


def count_words(subreddit, word_list, after='', word_counts={}):
    """
    Recursive function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    headers = {'User-Agent': 'alx-system_engineering-devops'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if after is None:
        # Sort and print the final word counts
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
        return

    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']
        for article in articles:
            title = article['data']['title'].lower()
            for word in word_list:
                # Count the occurrences of each word in the title
                occurrences = title.split().count(word.lower())
                if occurrences > 0:
                    word_counts[word.lower()] = word_counts.get(word.lower(), 0) + occurrences

        # Recursive call with the next page of articles
        count_words(subreddit, word_list, data['data']['after'], word_counts)
    else:
        if after == '':
            # Only print nothing if this is the first request
            print('', end='')


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())
