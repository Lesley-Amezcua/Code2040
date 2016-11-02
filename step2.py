import requests
import json

token = "a7af5887ffcb7da51f6dff6683736f30"
string = " "

#dictionary with token and string key
dict = {'token': token, 'string': string}

#requesting using post and json
req = requests.post("http://challenge.code2040.org/api/reverse", json=dict)

#retreve string content for testing purposes
print (req.content)

string = req.text
stringReverse = ''

#seting length of string to size
size = len(string)

for i in range(0, size):
    #the new string will now place the charater of original string to the new string
    stringReverse = string[i] + stringReverse

dict['string'] = stringReverse
req1 = requests.post("http://challenge.code2040.org/api/reverse/validate", json=dict)
#prints reversed string for testing purposes
print(req1.content)
