import requests
import json

token = "a7af5887ffcb7da51f6dff6683736f30"
github = "https://github.com/Lesley-Amezcua/Code2040"

#dictionary with token and github key
dict = {'token': token, 'github': github}

#requesting using post and json
req = requests.post("http://challenge.code2040.org/api/register", json=dict)

#printing json request for testing purposes
print (req.content)
