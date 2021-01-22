import random
import re
import requests

def bqb_url(count):   #传入需要多少张图片的参数
    count = count
    # 定义两个空集合存放抓取到的url地址
    Href = []
    target = []
    # api
    url = f'https://ovo.fghrsh.net/v1/?encode=html&src=category_emoticon/thumb_1/limit_{count}'

    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
    }
    # 响应数据
    response = requests.get(url=url, headers=headers)
    text = response.text

    # ex 为正则格式
    ex1 = 'href="(.*?)"'
    ex2 = '<img src="(.*?).th(.*?)"'

    target_url = []
    # 抓取到url返回列表格式
    Href = re.findall(ex1, text)
    target = re.findall(ex2, text)
    for i in range(0, len(target)):
        target_url.append(target[i][0] + target[i][1])

    return Href,target_url
    #万恶的防盗链，可以抓取但是bot无法发送