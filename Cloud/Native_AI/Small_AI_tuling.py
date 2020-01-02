import requests
import json

urls = 'http://openapi.tuling123.com/openapi/api/v2'

def respond(data):

    data_dict = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": data
            },
        },
        "userInfo": {
            "apiKey": 'a2afb9c136d64d22a63953f5d6aaf27a',
            "userId": 'SmallAI'
        }
    }

    result = requests.post(urls, json=data_dict)
    content = (result.content).decode('utf-8')
    str = json.loads(content)
    print('Small_AI:', str['results'][0]['values']['text'])

print("你好，我是Small_AI，有什么可以帮助你吗？")

while True:
    data = input('你：')
    respond(data)


#
#
# print(content)