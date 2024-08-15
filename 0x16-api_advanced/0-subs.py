#!/usr/bin/python3

"""
my python code extracts the number of
subscribers from a specific subreddit on Reddit
0-subs.py
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subs
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.102 Safari/537.36 Edg/115.0.1901.182'
    }

    try:
        r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)
        r.raise_for_status()  # Raises an HTTPError for bad responses
        subs = r.json().get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0

    return subs
