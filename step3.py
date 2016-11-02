import requests
import json
import ast
token = "a7af5887ffcb7da51f6dff6683736f30"
needle = " "


#dictionary with token and needle key
dict = {'token': token, 'needle': needle}

#requesting using post and json
req = requests.post("http://challenge.code2040.org/api/haystack", json=dict)
#retreve content for testing purposes
print (req.content)

index = 0
stri = req.content

#converts form unicode to dict
stri = ast.literal_eval(stri)


for i in stri['haystack']:
    if(stri['needle'] == i):
        break;
    else:
        index += 1

dict['needle'] = i
dict['needle'] = index
req1 = requests.post("http://challenge.code2040.org/api/haystack/validate", json=dict)
#prints content for testing purposes
print(req1.content)
