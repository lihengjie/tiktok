import requests
import hashlib
import time
import datetime
import json

# 测试环境
host = 'mercury.snssdk.com'

# 生产环境
# host = 'stream.feedcoopapi.com'

# curl --location --request POST 'mercury.snssdk.com/cooper/sync/third_upload?partner_id=1234&key_index=1&nonce=ibuaiVcKdpRxkhJA&time_stamp=1615866073439&sign=EE219A9F167884B338FADCD8211FB94A' \
# --header 'Content-Type: multipart/form-data' \
# --form 'input=@"/path/to/file"'

partner_id = '21'
key_index = '1'
secret_key = '192006250b4c09247ec02edce69f6a2d'

import hashlib


# md5加密
def md5String(in_str):
    md5 = hashlib.md5()
    md5.update(in_str.encode("utf8"))
    result = md5.hexdigest()
    return result



def getSign(paramStr):
    b = f'{paramStr}&key={secret_key}'
    print(b)
    sign = md5String(b).upper()
    print(sign)
    return sign

def getParamAndSign():
    time_stamp = str(int(round(time.time()*1000)))
    paramStr = f'key_index={key_index}&nonce=ibuaiVcKdpRxkhJA&partner_id={partner_id}&time_stamp={time_stamp}'
    sign = getSign(paramStr)
    return f'{paramStr}&sign={sign}'


def getResouceInfo(resoutcePath):
    paramAndSign = getParamAndSign()
    url = f'https://{host}/cooper/sync/third_upload?{paramAndSign}'

    print('url == '+url)

    files = {
        'input': open(resoutcePath,'rb')
    }
    headers = {'Content-Type': 'multipart/form-data'}
    # print(files)
    # res = requests.post(url=url,headers=headers,files=files)
    res = requests.post(url=url,files=files)
    print(res.text)
    return res.text

def getCoverUrl(picResourcePath):
    picRes = getResouceInfo(picResourcePath)
    print('上传图片Response:'+picRes)
    picRes = json.loads(picRes)
    coverUrl = picRes['image']
    return coverUrl

def getVedioId(vedioResourcePath):
    print('正在上传视频：'+vedioResourcePath)
    vedioRes = getResouceInfo(vedioResourcePath)
    print('上传视频Response：'+vedioRes)
    vedioRes = json.loads(vedioRes)
    videoId = vedioRes['video']
    return videoId


if __name__ == '__main__':
    print(1)
    # coverUrl = getCoverUrl()
    # videoId = getVedioId()
    # sendData = {"article_id":"123456","title":"测试","cover_urls":[coverUrl],"author_id":1,"video_id":videoId}
    #
    # paramAndSign = getParamAndSign()
    # url = f'https://{host}/cooper/sync/third_article?{paramAndSign}'
    #
    # headers = {'Content-Type': 'application/json'}
    #
    # res = requests.post(url=url,headers=headers,data=sendData)
    # print(res.text)



