# 导入json模块
import json

# 导入网络请求模块
import requests


# 简单请求
def get_url():
    # 发送网络请求
    response = requests.get('https://www.baidu.com')
    print('响应状态码：', response.status_code)
    print('请求的网络地址为：', response.url)
    print('头部信息：', response.headers)
    print('cookie信息为：', response.cookies)
    # 对响应结果进行utf-8编码
    response.encoding = 'utf-8'
    print(response.text)


# 带参请求
def get_url_params():
    data = {
        'name': 'Michael',
        'age': '36'
    }
    # response = requests.get('http://httpbin.org/get?name=Jack&age=30')
    response = requests.get('http://httpbin.org/get', params=data)
    print(response.text)


# post请求
def post_url():
    # 元组类型数据
    # data = (('1', '能力是有限的，而努力是无限的'), ('2', '星光不问赶路人，时光不负有心人'))
    # 列表类型数据
    # data = [('1', '能力是有限的，而努力是无限的'), ('2', '星光不问赶路人，时光不负有心人')]
    # 字典类型数据
    data = {'1': '能力是有限的，而努力是无限的', '2': '星光不问赶路人，时光不负有心人'}
    # 将字典类型转换为JSON类型的表单数据
    # data = json.dumps(data)
    response = requests.post('http://httpbin.org/post', data=data)
    response_dict = json.loads(response.text)
    print(response_dict)


def get_bytes():
    response = requests.get('https://www.baidu.com/img/bd_logo1.png?where=super')
    # 打印二进制数据
    print(response.content)
    # 通过open函数将二进制数据写入本地文件
    with open('../百度logo.png', 'wb') as f:
        f.write(response.content)


# 复杂的网络请求
def complex_url():
    url = 'https://www.baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36 '
    }
    res = requests.get(url, headers=headers)
    print(res.status_code)


if __name__ == '__main__':
    # get_url()
    # get_bytes()
    # get_url_params()
    # post_url()
    complex_url()
