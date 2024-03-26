# api call
import requests
from dotenv import load_dotenv
import os

load_dotenv()
#
# username = os.getenv("email")
# password = os.getenv("password")
# url = "https://kishankumarvm.atlassian.net/rest/agile/1.0/board/4/sprint/2/issue"


def get_boardid(jira_url, email, password):
    board_id = []
    url = f"{jira_url}/rest/agile/1.0/board/"
    print(url)
    try:
        response = requests.get(url, auth=(email, password))
        for value in response.json()['values']:
            board_id.append([value['id'], value['name']])
        return board_id
    except Exception as e:
        print(f"Error: {e}")
        return board_id


def get_sprintid(jira_url, email, password, board_id):
    sprint_id = []
    url = f"{jira_url}/rest/agile/1.0/board/{board_id}/sprint/"
    print(url)
    try:
        response = requests.get(url, auth=(email, password))
        for value in response.json()['values']:
            if value['state'] == 'active':
                sprint_id.append([value['id'], value['name']])
        return sprint_id
    except Exception as e:
        print(f"Error: {e}")
        return sprint_id


def get_issues(jira_url, email, password, board_id, sprint_id):
    user_story = []
    url = f"{jira_url}/rest/agile/1.0/board/{board_id}/sprint/{sprint_id}/issue"
    print(url)
    try:
        response = requests.get(url, auth=(email, password))
        for issue in response.json()['issues']:
            if issue['fields']['sprint']['state'] == 'active':
                user_story.append(issue['fields']['description'])
        return user_story
    except:
        return user_story
