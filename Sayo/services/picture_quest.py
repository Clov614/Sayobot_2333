import random
import string
from bs4 import BeautifulSoup
import lxml
import requests
import re
import base64
import random
import string
def picture_get():
    headers ={
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
     }

    # pic_url = 'https://img.fghrsh.net/?random'
    pic_url = 'https://i.xinger.ink:4443/images.php'

    r1 = random.choice(range(0,10000)and string.ascii_lowercase and string.ascii_uppercase)
    r3 = random.choices(range(0, 10000) and string.ascii_lowercase and string.ascii_uppercase, k=3)
    r_a = r1+r3[0]+r3[1]+r3[2]
    pic_url = f'https://i.xinger.ink:4443/images.php?{r_a}'
    # response = requests.get(url=pic_url,headers=headers)
    # response.encoding = 'utf-8'
    # page_text = response.text
    #
    #
    # s1 = r'^<link rel="image_src" href="https://[/s/S]*">$'
    # ex = r'<link.*?<img src="(.*?)"alt=.*?/>'
    # ex2 = 'src="(.*?)"'
    # m1 = re.findall(ex2,page_text,re.S)
    # # print(len(m1))
    # s = r'\.jpg'
    # for i in range(0,len(m1)):
    #     if(re.search(s,m1[i]) != None):
    #         target_url = m1[i]
    #         break
    # return target_url
    return pic_url


    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
    # }
    #
    # pic_url = 'https://i.xinger.ink:4443/images.php'
    # response = requests.get(url=pic_url, headers=headers)
    # response.encoding = 'utf-8'
    # page_text = response.content
    # print(page_text)
    # with open('./sources/img.jpg', 'wb') as f:
    #     f.write(page_text)
    #     f.close()
