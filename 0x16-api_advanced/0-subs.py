#!/usr/bin/python3

"""
my python code extracts the number of
subscribers from a specific subreddit on Reddit
0-subs.py
"""
import requests

def number_of_subscribers(subreddit):
    """NUMBER OF SUBS"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    
    headers = {'User-Agent': 'aLX/1.0'}
    
    try:
        r = requests.get(f'http://www.reddit.com/r/{subreddit}/about.json', headers=headers)
        r.raise_for_status()
        subs = r.json().get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
    
    return subs
