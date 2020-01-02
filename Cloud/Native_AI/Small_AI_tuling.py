import requests
import json
import webbrowser

from aip import AipSpeech
import playsound

urls = 'http://openapi.tuling123.com/openapi/api/v2'

def respond(data):

    if '我想听歌' in data:
        douban_url = 'https://douban.fm/'
        webbrowser.get().open(douban_url)

    if '我想搜索' in data:
        keywords = input("请输入你要搜索的关键词：")
        baidu_url = 'https://www.baidu.com/s?wd=' + keywords
        webbrowser.get().open(baidu_url)

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

""" 你的 APP AK SK """
APP_ID = '18162730'
API_KEY = 'LQizcGxUzY26PdXBhEd66x5z'
SECERT_KEY = 'Afrj8rWv2kdYhMTrLaX3OLUu8oZpsZ0x'

client = AipSpeech(APP_ID, API_KEY, SECERT_KEY)

def small_AI_speak(data):
    result = client.synthesis('你今天真好看', 'zh', 1, {
        'vol': 5,
        'per': 4,  # beatuiful
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb', ) as f:
            f.write(result)

    playsound.playsound('audio.mp3')

small_AI_speak(str['results'][0]['values']['text'])
# print('small_AI_speak:',str['results'][0]['values']['text'])
#
# print(content)