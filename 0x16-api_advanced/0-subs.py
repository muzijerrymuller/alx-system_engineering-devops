#!/usr/bin/python3

"""
Returns the number of subscribers for a given subreddit.
If the subreddit is invalid, returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    headers = {'User-Agent': 'python:subscribers.counter:v1.0.0 (by /u/yourusername)'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
