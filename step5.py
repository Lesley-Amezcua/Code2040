import requests
import json
import ast
import datetime

token = "a7af5887ffcb7da51f6dff6683736f30"
datestamp = ''

#dictionary with token and datestamp key
dict = {'token': token, 'datestamp': datestamp}

#requesting using post and json
req = requests.post("http://challenge.code2040.org/api/dating", json=dict)
#prints contents for testing purposes
print(req.content)

#converts form unicode to dict
time = ast.literal_eval(req.text)
#holds the iso 8601 value
dateTime = '%Y-%m-%dT%H:%M:%SZ'

date = time['datestamp']

interval = time['interval']

#gets the time from string of time
realTime = datetime.datetime.strptime(date, dateTime)

#adds seconds
interval = long(interval)
realTime = realTime + datetime.timedelta(seconds = interval)
results = realTime.isoformat()
results = str(results) + 'Z'

dict['datestamp'] = results
req1 = requests.post("http://challenge.code2040.org/api/dating/validate", json=dict)
#prints contents for testing purposes
print(req1.content)
