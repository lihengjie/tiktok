import os
import json
import requests
import SendVideo
import random


# path = '/Users/lihengjie/Downloads/test_upload'
path = '/Volumes/mac资料/douyin_download/杀神将军陆炎/'

sensitiveWordList = ['抖音', 'dou+', 'DOU+', 'dou来', 'DOU来', '直播小助手', '抖来', '西瓜视频', '懂车帝']
userList = [2023001,2023002,2023003,2023004,2023005,2023006,2023007,2023008,2023009,20230010]



if __name__ == '__main__':

    for root, dirs, files in os.walk(path):
        # todo if not dir
        for dir in dirs:
            for root_d,dirs_d,files_d in os.walk(os.path.join(root,dir)):
                videoPath = ''
                coverPath = ''
                videoCoverUrl = ''
                videoId = ''
                videoDesc = ''
                for file in files_d:
                    try:
                        if file == 'result.json':
                            with open(os.path.join(root_d,file)) as resultFile:
                                print(os.path.join(root_d,file))
                                resultContent = resultFile.read()
                                resultJson = json.loads(resultContent)

                                videoDesc = resultJson['desc']
                                videoId = resultJson['aweme_id']
                                print(videoDesc)
                                print(videoId)
                                # videoCoverUrlList = resultJson['video']['cover']['url_list']
                                # for cover in videoCoverUrlList:
                                #     if cover.find('jpeg') != -1:
                                #         videoCoverUrl = cover
                                # print(videoCoverUrl)

                                # if videoCoverUrl is not None:
                                #     coverPath = os.path.join(root_d,file)[:-11]+'cover.jpeg'
                                #     coverRes = requests.get(videoCoverUrl)
                                #     with open(coverPath,'wb') as coverImg:
                                #         coverImg.write(coverRes.content)

                        elif file[-3:] == 'mp4':
                            videoPath = os.path.join(root_d,file)
                            print(videoPath)
                        elif file == 'cover.jpeg':
                            coverPath = os.path.join(root_d,file)
                    except Exception:
                        continue
                    #     upload
                if videoPath != '' and coverPath != '' and videoId != '' and videoDesc != '':
                    coverUrl = SendVideo.getCoverUrl(coverPath)
                    videoId = SendVideo.getVedioId(videoPath)

                    if coverUrl == '' or videoId == '':
                        continue

                    for i in range(len(sensitiveWordList)):
                        if videoDesc.find(sensitiveWordList[i]) != -1:
                            videoDesc = videoDesc.replace(sensitiveWordList[i], '')

                    sendData = {
                        "article_id": videoId,
                        "title": videoDesc,
                        "cover_urls": [coverUrl],
                        "author_id": userList[random.randint(0,len(userList)-1)],
                        "video_id": videoId
                    }

                    sendData = json.dumps(sendData)

                    paramAndSign = SendVideo.getParamAndSign()
                    url = f'https://{SendVideo.host}/cooper/sync/third_article?{paramAndSign}'

                    headers = {'Content-Type': 'application/json'}

                    res = requests.post(url=url, headers=headers, data=sendData)
                    print(res.text)
                    res = json.loads(res.text)
                    if res['msg'] == 'success':
                        print('发布成功：' + videoPath)


                    # print(os.path.join(root,dir))