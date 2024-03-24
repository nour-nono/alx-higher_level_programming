#!/usr/bin/python3
"""Show the lastone ten commits in a repo github"""
if __name__ == "__main__":
    import requests
    import sys
    u = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[0]}/commits"
    r = requests.get(u)
    count = 0
    for i in r.json():
        print(f"{i.get('sha')}: {i.get('commit').get('author').get('name')}")
        if count > 9:
            break
