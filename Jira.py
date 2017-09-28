
import json
from jira.client import JIRA
options  = {'server':'https://fujitsuautomationcenter.atlassian.net'}
jira = JIRA(options,basic_auth=('biju.oommen@us.fujitsu.com', 'Fujitsu2017!'))
#issue=jira.issue('JAR-1330')
projects=jira.projects()
print([item.key for item in projects])
issue=jira.issue('FAC-1')
print(issue.self)
print(issue.fields.summary)
print(issue.fields.status)
issuenew=jira.create_issue(project={'key':'FAC'},summary='Splunk Created Issue',
                          description='Batch Job Failed',issuetype={'name':'Bug'})
print(issuenew.self)
