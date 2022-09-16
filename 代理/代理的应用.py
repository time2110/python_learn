import json
import re

import pandas
import requests
from lxml import etree
import pandas as pd


# 通过代理发送请求
def proxy_url():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36 '
    }

    proxy = {
        'http': 'http://117.88.176.38:3000',
        'https': 'https://117.88.176.38:3000'
    }
    try:
        res = requests.get('http://2020.ip138.com', headers=headers, proxies=proxy, verify=False, timeout=3)
        print(res.status_code)
    except Exception as e:
        print('错误信息：', e)


# 获取免费代理ip
def free_proxy():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36 ',
    }
    res = requests.get('http://proxylist.fatezero.org/proxy.list', headers=headers)
    if res.status_code == 200:
        res = res.text
        li = []
        while True:
            s = res.find("{")
            s1 = res.find("}")
            if s1 == -1:
                break
            li.append(eval(res[s:s1 + 1]))
            res = res[s1 + 1:]

        ip_table = pd.DataFrame(columns=['ip'])
        ip_list = []
        for i in li:
            # print(i['host'], i['port'])
            ip_list.append(i['host'] + ':' + str(i['port']))
        ip_table['ip'] = ip_list
        ip_table.to_excel('ip.xlsx', sheet_name='data')
    # table = re.findall('"host": "(\d+?.\d+?.\d*?.\d*?)", "port": (\d+)', res.text)
    # print(table)
    # if res.status_code == 200:
    #     table = re.findall('<td>(\d+?.\d+?.\d*?.\d*?)</td><td>(\d+?)</td>', res.text)
    #     print(table)
    #     ip_table = pd.DataFrame(columns=['ip'])
    #     ip_list = []
    #     for t in table:
    #         ip = t[0]
    #         port = t[1]
    #         ip_list.append(ip + ':' + port)
    #         print('代理IP为：', ip, '对应端口号为：', port)
    #
    #     ip_table['ip'] = ip_list
    #     # 将提取的Ip保存Excel文件ip列
    #     ip_table.to_excel('ip.xlsx', sheet_name='data')


# 检测代理Ip是否有效
def check_proxy():
    ip_table = pandas.read_excel('ip.xlsx')
    ip = ip_table['ip']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36 '
    }
    ip_true = []
    for i in ip:
        proxies = {
            'http': 'http://{ip}'.format(ip=i),
            'https': 'https://{ip}'.format(ip=i)
        }

        try:
            res = requests.get('http://2022.ip138.com/', headers=headers, proxies=proxies, timeout=2)
            if res.status_code == 200:
                res.encoding = 'utf-8'
                html = etree.HTML(res.text)
                info = html.xpath('/html/body/p[1]/a/text()')
                # print(proxies)
                ip_true.append(i)
                print(i)
                # print('ip地址：', info[0].strip())
        except Exception as e:
            pass

    ip_table = pd.DataFrame(columns=['ip'])
    ip_table['ip'] = ip_true
    ip_table.to_excel('ip_true.xlsx', sheet_name='data')


if __name__ == '__main__':
    # proxy_url()
    # free_proxy()
    check_proxy()
