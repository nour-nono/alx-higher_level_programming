#!/usr/bin/python3
"""Show the lastone ten commits in a repo github"""
import requests
from sys import argv

if __name__ == "__main__":
    import requests
    u = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[0]}/commits"
    r = requests.get(url=u)
    for i in range(10):
	    print(r.json()[i]['sha'], r.json()[i]['commit']['author']['name'])
