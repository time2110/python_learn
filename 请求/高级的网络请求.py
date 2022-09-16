import pandas as pd
import requests_cache
import requests
import time
from requests_html import HTMLSession, UserAgent
import re

version = requests_cache.__version__
print('模块版本为：', version)


# 判断是否存在请求缓存
def check_cache():
    requests_cache.install_cache()
    url = 'http://httpbin.org/get'
    r = requests.get(url)
    print('是否存在缓存：', r.from_cache)
    requests_cache.clear()
    r = requests.get(url)
    print('是否存在缓存：', r.from_cache)


# 判断是否需要设置延时操作
def time_cache():
    # 定义钩子函数
    def make_throttle_hook(timeout=0.1):
        def hook(response, *args, **kwargs):
            print(response.text)
            # 没有缓存就加延时
            if not getattr(response, 'from_cache', False):
                print('等待', timeout, '秒！')
                time.sleep(timeout)
            else:
                print('请求缓存', response.from_cache)
            return response

        return hook

    # 创建缓存
    # backend 设置不同的存储机制 memory sqlite monggo redis
    requests_cache.install_cache(backend='sqlite')
    # 清理缓存
    requests_cache.clear()
    # 创建缓存会话
    s = requests_cache.CachedSession()
    s.hooks = {'response': make_throttle_hook(2)}
    url = 'http://httpbin.org/get'
    s.get(url)
    s.get(url)


# 强大的Requests-HTML模块 GET请求
def get_html_url():
    # 创建HTML会话对象
    session = HTMLSession()
    # 创建随机请求头
    ua = UserAgent().random
    url = 'http://httpbin.org/get'
    r = session.get(url, headers={'user-agent': ua})
    print(r.text)


# 强大的Requests-HTML模块 POST请求
def post_html_url():
    session = HTMLSession()
    data = {
        'user': 'admin',
        'password': 123456
    }
    r = session.post('http://httpbin.org/post', data=data)
    print(r.text)


# 数据的提取
# 1、css选择器 find(selector,containing) 参数：css选择器，指定网页元素包含的内容
# 2、xpath选择器 xpath(selector)
# 3、search()与search_all()

# 爬取即时新闻
def get_news():
    session = HTMLSession()
    ua = UserAgent().random
    r = session.get('http://news.youth.cn/jsxw/index.htm', headers={'user-agent': ua})
    r.encoding = 'gb2312'
    if r.status_code == 200:
        # li_all = r.html.xpath('/html/body/div[3]/div[1]/div[1]/ul/li')
        # for li in li_all:
        # news_title = li.find('a')[0].text
        # news_href = 'http://news.youth.cn/jsxw' + li.find('a[href]')[0].attrs.get('href').lstrip('.')
        # news_time = li.find('font')[0].text

        # a = li.search('<a href="{}">{}</a>')
        # news_title = a[1]
        # news_href = 'http://news.youth.cn/jsxw' + a[0]

        news = re.findall('<font>(.*?)</font><a href="(.*?)">(.*?)</a>', r.text)
        news_title = []
        news_href = []
        news_date = []
        for n in news:
            news_title.append(n[2])
            news_href.append('http://news.youth.cn/jsxw' + n[1])
            news_date.append(n[0])

        table = pd.DataFrame(columns=['时间', '标题', '链接'])
        table['时间'] = news_date
        table['标题'] = news_title
        table['链接'] = news_href
        table.to_excel('news.xlsx', sheet_name='data')


#  获取动态加载的数据


if __name__ == '__main__':
    # check_cache()
    # time_cache()
    # get_html_url()
    # post_html_url()
    get_news()
