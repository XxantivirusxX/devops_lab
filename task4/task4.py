import requests
import json
import getpass


print("Username")
username = input()
passwd = getpass.getpass()
print("Index")
ind = int(input())
url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'
gre = requests.get(url, auth=(username, passwd)).json()
print("Title: %s" % gre[ind]['title'],)
print("State: %s " % gre[ind]['state'])
print("Owner's login: %s " % gre[ind]['head']['repo']['owner']['login'])
print("Created: %s " % gre[ind]['head']['repo']['created_at'])
print("Updated: %s " % gre[ind]['head']['repo']['updated_at'])
print("Repo name: %s " % gre[ind]['head']['repo']['name'])
print("Owner's url: %s " % gre[ind]['base']['repo']['owner']['url'])

