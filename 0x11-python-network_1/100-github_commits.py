#!/usr/bin/python3
"""Show the lastone ten commits in a repo github"""
if __name__ == "__main__":
    import requests
    import sys
    u = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[0]}/commits"
    r = requests.get(u)
    for i in range(10):
	    print(r.json()[i]['sha'], r.json()[i]['commit']['author']['name'])
