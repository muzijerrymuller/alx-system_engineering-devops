#!/usr/bin/python3

"""
prints first dedicated amout of posts
"""

import requests

def top_ten(subreddit):
    """
    prints the first dedicated amount of posts
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.102 Safari/537.36 Edg/115.0.1901.182'
    }
    
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        if response.status_code == 200:
            results = response.json().get("data", {}).get("children", [])
            if not results:
                print("None")
            else:
                for post in results:
                    print(post.get("data", {}).get("title"))
        else:
            print("None")

    except requests.exceptions.HTTPError:
        print("None")
    except requests.exceptions.RequestException:
        print("None")
    except ValueError:
        print("None")
