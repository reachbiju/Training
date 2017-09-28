
import json
from jira.client import JIRA
options  = {'server':'https://fujitsuautomationcenter.atlassian.net'}
jira = JIRA(options,basic_auth=('biju.oommen@us.fujitsu.com', 'Fujitsu2017!'))
projects=jira.projects()
issue=jira.create_issue(project={'key':'FAC'},summary='Fujitsu Automation Cente - Batch Job',
                          description='Batch Job Failed-  Pick to Ship',issuetype={'name':'Bug'})
