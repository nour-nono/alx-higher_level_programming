#!/usr/bin/python3
""" A Python script that takes your GitHub
credentials (username and personal access token)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(url=f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits")
    for i in range(10):
	      print(r.json()[i]['sha'], r.json()[i]['commit']['author']['name'])
