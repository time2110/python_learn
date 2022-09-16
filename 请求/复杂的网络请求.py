import requests
# 导入 HTTPBasicAuth 类
from requests.auth import HTTPBasicAuth
# 导入 requests.exceptions 模块中的3种异常类
from requests.exceptions import ReadTimeout, HTTPError, RequestException

from lxml import etree


# 验证cookie
def cookies_url():
    headers = {
        'Cookie': 'bid=zVkUHHuXmgg; _ga=GA1.1.861879757.1656643821; '
                  '_ga_RXNMP372GL=GS1.1.1656643820.1.1.1656643909.60; '
                  '__utma=30149280.861879757.1656643821.1659061285.1659061285.1; '
                  '__utmz=30149280.1659061285.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118281"; '
                  'dbcl2="172630432:4cxmKPB0wMI"; push_noty_num=0; push_doumail_num=0; ck=YgFP; ap_v=0,6.0',
        'Host': 'www.douban.com',
        'Referer': 'https://www.douban.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36 '
    }
    # cookies_jar = requests.cookies.RequestsCookieJar()
    # for cookie in cookies.split(';'):
    #     key, value = cookie.split('=', 1)
    #     cookies_jar.set(key, value)

    res = requests.get('https://www.douban.com/', headers=headers,  # cookies=cookies_jar
                       )
    if res.status_code == 200:
        html = etree.HTML(res.text)
        name = html.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]')
        print(name[0].text)


# 会话请求
def session_url():
    s = requests.Session()
    data = {
        'email': '498759996@qq.com',
        'passwd': '12345678'
    }
    res1 = s.post('https://go.tofly.cyou/auth/login', data=data)
    res2 = s.get('https://go.tofly.cyou/user')
    print('登录信息：', res1.text)
    print('登录后页面信息如下：\n', res2.text)


# 验证请求
def auth_url():
    url = 'http://sck.rjkflm.com:6666/spider/auth/'
    ah = HTTPBasicAuth('admin', 'admin')
    res = requests.get(url, auth=ah)
    if res.status_code == 200:
        print(res.text)


# 网络超时与异常
def timeout_url():
    for a in range(0, 50):
        try:
            res = requests.get('https://www.baidu.com/', timeout=0.1)
            print(res.status_code)
        except Exception as e:
            print('异常' + str(e))


# 网络异常分类
def error_url():
    for a in range(0, 50):
        try:
            res = requests.get('https://www.baidu.com/', timeout=0.01)
            print(res.status_code)
        except ReadTimeout:
            print('请求超时')
        except HTTPError:
            print('HTTP异常')
        except RequestException:
            print('请求异常')


# 上传图片文件
def file_url():
    bd = open('../百度logo.png', 'rb')
    file = {
        'file': bd
    }
    res = requests.post('http://httpbin.org/post', files=file)
    print(res.text)


if __name__ == '__main__':
    cookies_url()
    # session_url()
    # auth_url()
    # timeout_url()
    # error_url()
    # file_url()
