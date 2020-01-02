

print("你好，我是Small_AI，有什么可以帮助你吗？")

def respond(data):
    if data in 'Adil':
        print('Small_AI：' + '世界上怎么会有这么好看的人？')
    if data in '谁最帅':
        print('Small_AI：' + '当然是你啦！')
    if data in '舔狗不得house':
        print('Small_AI：' + '我这说的是事实啊！')
    if data in '886':
        print('Small_AI：' + '再见！爱你哟！')


while True:
    data = input('你：')
    respond(data)
    # data = data.replace('我','你')
    # print('Small_AI:' + data.strip('吗？') + '!')



