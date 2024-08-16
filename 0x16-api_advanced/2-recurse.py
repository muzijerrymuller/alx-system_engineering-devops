#!/usr/bin/python3




"""
A recursive approach to fetch all hot article titles from Reddit
for a specific subreddit using the Reddit API.
AND THEN Returns None if the subreddit has no content.
"""





def recurse(subreddit, hot_list=[], after=""):
    """
    Interacts with the Reddit API to retrieve
    a list of titles for all hot posts in a specified subreddit.
    AND THEN Returns None if the subreddit is invalid.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
