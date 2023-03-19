import string
import random

sensitiveWordList = ['抖音', 'dou+', 'DOU+', 'dou来', 'DOU来', '直播小助手', '抖来', '西瓜视频', '懂车帝']
userList = [2023001,2023002,2023003,2023004,2023005,2023006,2023007,2023008,2023009,20230010]


def test(n):
    '''生成长度为 n 的随机账号'''
    # 数字+大小写字母组合
    s = string.digits + string.ascii_letters
    words = random.sample(s, n)
    return ''.join(words)


if __name__ == '__main__':
    for i in range(10):
        # print(test(16))
        print(userList[random.randint(0,len(userList)-1)])
    a = 'abcdefdou+抖音777抖来'
    a = a.replace('bc','')
    print(a)
    

    for i in range(len(sensitiveWordList)):
        if a.find(sensitiveWordList[i]) != -1:
            a = a.replace(sensitiveWordList[i],'')
            print(a)



