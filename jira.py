# api call
import requests
from dotenv import load_dotenv
import os

load_dotenv()
#
# username = os.getenv("email")
# password = os.getenv("password")
# url = "https://kishankumarvm.atlassian.net/rest/agile/1.0/board/4/sprint/2/issue"


def get_issues(jira_url, email, password):
    user_story = []
    # url = "https://kishankumarvm.atlassian.net/rest/agile/1.0/board/4/sprint/2/issue"
    try:
        response = requests.get(jira_url, auth=(email, password))
        for issue in response.json()['issues']:
            if issue['fields']['sprint']['state'] == 'active':
                user_story.append(issue['fields']['description'])
        return user_story
    except:
        return user_story
