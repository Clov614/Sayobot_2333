import requests
import os
import base64
import random
import string
import re
class Pixiv():
    def __init__(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
        }
        params = {
            'file': '(binary)',
            'url': 'https://i.xinger.ink:4443/images.php?kb',
            'frame': '1',
            'hide': '0',
            'database': '999',
        }
    def Pixivid_get(url): #传入从QQ消息获取到的图片url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
        }
        params = {
            'file': '(binary)',
            'url': 'https://i.xinger.ink:4443/images.php?kb',
            'frame': '1',
            'hide': '0',
            'database': '999',
        }

        params['url'] = url  # 将url传入params
        pic_url = 'https://saucenao.com/search.php' #图片查询网站接口
        response = requests.get(url=pic_url, headers=headers, params=params) # 发起get请求
        response.encoding = 'utf-8'
        page_text = response.text
        news = page_text
        # 正则将图片的pixivid以及网站抓出
        ex = '>Pixiv #(.*?)</a><br'
        date1 = re.findall(ex, news, re.S)
        # print(date1[0])
        ex2 = 'class="resulttitle"><strong>(.*?)</strong><br /></div><div'
        date2 = re.findall(ex2, news, re.S)
        # print(date2[0])
        ex3 = 'ID: </strong><a href="(.*?)" class='
        date3 = re.findall(ex3, news, re.S)
        # print(date3[0])
        ex4 = 'raw-rating="1" src="(.*?)"'
        date4 = re.findall(ex4, news, re.S)
        # print(date4[0])
        ex5 = '<div class="resultsimilarityinfo">(.*?)</div>'
        date5 = re.findall(ex5, news, re.S)
        # print(date5[0])
        totle = [] #空集合存抓到的数据
        totle.append(date1[0])
        totle.append(date2[0])
        totle.append(date3[0])
        totle.append(date4[0])
        totle.append(date5[0])
        # try:
        #     totle.append(date1[0])
        #     totle.append(date2[0])
        #     totle.append(date3[0])
        #     totle.append(date4[0])
        #     totle.append(date5[0])
        # except IndexError:
        #     pass
        # if totle == None:
        #     totle.append('错误，请重试！')
        #     totle.append('错误，请重试！')
        #     totle.append('错误，请重试！')
        #     totle.append('错误，请重试！')
        #     totle.append('http://fp1.fghrsh.net/2021/01/10/d1c1e09f6c9448da221cb688a1b66b3d.jpg')

        return totle  #返回抓到的数据

    def m_ke(pic):
        pic = pic
        ex = 'url=(.*?)term'
        pic_url = re.findall(ex,pic)
        pic_get = pic_url[0]
        with open('./sources/pic_pixiv.db','w',encoding='utf-8') as fp:
            # fp.write(pic_get)
            fp.write(pic_get)
            fp.close()

        return pic_get


