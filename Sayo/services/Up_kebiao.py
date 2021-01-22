
import re


class KB():
    def m_ke(pic):  #存课表方法，课表保存于sources目录下
        pic = pic
        ex = 'url=(.*?)term'
        pic_url = re.findall(ex,pic)
        pic_get = pic_url[0]
        with open('./sources/pic.db','w',encoding='utf-8') as fp:
            # fp.write(pic_get)
            fp.write(pic_get)
            fp.close()

        return pic_get

    def del_KeBiao(self): #删除课表方法
        open('./sources/pic.db','w',encoding='utf-8').close()


    def url_output(self): #读取课表
        with open('./sources/pic.db','r') as fp:
            image_url = fp.read()
            fp.close()

            return image_url

