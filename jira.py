# api call
import requests
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("email")
password = os.getenv("password")


def get_issues():
    user_story = []
    url = "https://kishankumarvm.atlassian.net/rest/agile/1.0/board/4/sprint/2/issue"
    try:
        response = requests.get(url, auth=(username, password))
        for issue in response.json()['issues']:
            if issue['fields']['sprint']['state'] == 'active':
                user_story.append(issue['fields']['description'])
        print(user_story)
        return user_story
    except:
        return user_story
