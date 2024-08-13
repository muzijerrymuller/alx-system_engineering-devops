#!/usr/bin/python3

"""
my python code extracts the number of
subscribers from a specific subreddit on Reddit
0-subs.py
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MuziMuller/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        results = data.get("data", {})
        return results.get("subscribers", 0)
    except (ValueError, KeyError):
        return 0
