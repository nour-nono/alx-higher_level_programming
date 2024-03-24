#!/usr/bin/python3
"""Show the lastone ten commits in a repo github"""
if __name__ == "__main__":
    import requests
    import sys
    u = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[0]}/commits"
    r = requests.get(u)
    count = 0
    for i in r.json():
        sha = i.get("sha")
        auth = i.get("commit").get("author").get("name")
        print(f'{sha}: {auth}')
        count += 1
        if count > 9:
            break
