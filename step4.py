import requests
import json
import ast
token = "a7af5887ffcb7da51f6dff6683736f30"
array = ''

#dictionary with token and array key
dict = {'token': token, 'array': array}

#requesting using post and json
req = requests.post("http://challenge.code2040.org/api/prefix", json=dict)

#converts form unicode to dict
array = ast.literal_eval(req.text)

#getting prefix
prefix = array[array.keys()[0]]

#sets length of prefix to size
size = len(prefix)

#Final Array
finArray = []

#traverse through the array to check if prefix exists in the code
for i in range(len(array['array'])):
    if prefix != array['array'][i][:size]:
        finArray.append(array['array'][i])

dict['array'] = finArray
req1 = requests.post("http://challenge.code2040.org/api/prefix/validate", json=dict)
#print contents for testing purposes
print(req1.content)
