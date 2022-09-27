import requests
import time
import random
import os
import re

json_url = 'https://www.skypixel.com/api/v2/works?lang=zh-Hans&platform=web&device=desktop&sort=hot&filter=featured:true&limit=20&offset=0'


class Crawl:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/105.0.0.0 Safari/537.36 '
        }

    def get_json(self, json_url1):
        res = requests.get(json_url1, headers=self.headers)
        if res.status_code == 200:
            return res.json()
        else:
            print('获取不成功')

    def download_video(self, video1):
        res = requests.get(video1['url'], headers=self.headers)
        if not os.path.exists('video'):
            os.mkdir('video')
        if res.status_code == 200:
            with open('video/' + video1['title'] + '.mp4', 'wb') as f:
                for data in res.iter_content(chunk_size=1024):
                    f.write(data)
                    f.flush()
                print('下载完成')
        else:
            print('下载失败')


if __name__ == '__main__':
    c = Crawl()
    for page in range(1):
        json = c.get_json(json_url.format(offset=page))
        infos = json['data']['items']
        video_arr = []
        for info in infos:
            if info['type'] != 'photo':
                video_arr.append({
                    'title': info['title'],
                    'url': info['cdn_url']['large']
                })
        print('视频总数：', video_arr.length)
        for video in video_arr:
            c.download_video(video)
