import requests
import re

#因为找不到持续监听消息的方法故荒废的blibli分享连接分析方法
def blibli_get(url):
    headers ={
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
         }

    # url = 'https://b23.tv/PHc6n0'
    # url2 = 'https://b23.tv/dtU1cn'
    response = requests.get(url=url,headers=headers)
    page_text = response.text
    # print(page_text)

    ex = 'itemprop="name" name="title" content="(.*?)">'
    target_title = re.findall(ex,page_text,)

    ex2 ='</span><span title="投硬币枚数(.*?)"'
    target_coin = re.findall(ex2,page_text,re.S)

    ex3 = ' class="view">(.*?) · </span><span title="(.*?)" class="dm">(.*?)</span>'
    target_play = re.findall(ex3,page_text,re.S)
    ex4 = '<span title="点赞数(.*?)" class'
    target_dianzan = re.findall(ex4,page_text,re.S)


    ex5 = '<span title="收藏人数(.*?)"'
    target_shoucang = re.findall(ex5,page_text,re.S)

    ex6 = '<meta data-vue-meta="true" itemprop="image" content="(.*?)"'
    target_pic_url = re.findall(ex6,page_text,re.S)


    total = f"""标题：{target_title[0]}
    播放数：{target_play[0][0]}  {target_play[0][1]}  投币数：{target_coin[0]}
    点赞数：{target_dianzan[0]}  收藏数：{target_shoucang[0]}
    
    """
    total_all = [total,target_pic_url]
    # print(total_all)
    return total_all  # 这边返回抓取的blibli分享数据的集合

