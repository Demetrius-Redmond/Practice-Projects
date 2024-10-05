from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

github_key = os.environ.get("GITHUB_API_KEY")

headers = {
    "Authorization" : "token {}".format(github_key),
    "Accept" : "application/vnd.github.sailor-v-preview+json"
 }
data = {
    "title" : "PullRequest-Using-GithubAPI",
    "body"  : "Pull Request test with api",
    "head"  : "pull-request", 
    "base"  : "master"
 }

username = input("Enter your Github username: ")
RepositoryName = input("Enter the name of your repository: ")

url = "https://api.github.com/repos/{}/{}/pulls".format(username, RepositoryName)

requests.post(url, data=json.dumps(data), headers=headers)