#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest)
of a given repository by a specified user.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{ow_name}/{repo_name}/commits"
    response = requests.get(url)

    commits = response.json()[:10]

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
