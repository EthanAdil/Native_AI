from aip import AipSpeech

""" 你的 APP AK SK """
APP_ID = '18162730'
API_KEY = 'LQizcGxUzY26PdXBhEd66x5z'
SECERT_KEY = 'Afrj8rWv2kdYhMTrLaX3OLUu8oZpsZ0x'

client = AipSpeech(APP_ID, API_KEY, SECERT_KEY)

result = client.synthesis('你今天真好看', 'zh', 1, {
    'vol' : 5,
    'per' : 4, # beatuiful
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3','wb',) as f:
        f.write(result)