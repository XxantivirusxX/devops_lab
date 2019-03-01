import requests
import getpass
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('username')
parser.add_argument('url', help="URL")
parser.add_argument('--title', '-t', action="store_true", help="Show title")
parser.add_argument('--state', '-s', action="store_true", help="State of PR")
parser.add_argument((
'--created_at', '-c', action="store_true", help="Creation time"))
parser.add_argument(( 
'--updated_at', '-u', action="store_true", help="Updated time"))
parser.add_argument('--ownerurl', '-o', action="store_true", help="Owner URL")
parser.add_argument('--repo', '-r', action="store_true", help="Repo name")
args = parser.parse_args()
passwd = getpass.getpass()
username = args.username
url = args.url


def repo_info(uname, pwd):
    gre = requests.get(url, auth=(username, passwd)).json()
    if args.title:
        print("Title: %s " % str(gre['title']))
    if args.state:
        print("State: %s " % gre['state'])
    if args.created_at:
        print("Creation time: %s " % str(gre['created_at']))
    if args.updated_at:
        print("Updation time: %s " % str(gre['updated_at']))
    if args.ownerurl:
        print(
            "Owner URL: %s " % str(gre['base']['repo']['owner']['html_url']))
    if args.repo:
        print("Repo name: %s " % gre['head']['repo']['name'])


if __name__ == '__main__':
    repo_info(username, passwd)
