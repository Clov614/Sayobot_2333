from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

from services.pixiv_img_analysis import Pixiv
from aiocqhttp.message import MessageSegment

__plugin_name__ = 'pixiv_analysis(pixiv图片检索)'
__plugin_usage__ = (
    '用法：\n'
    '对我说 “sayo pixiv” 后传入图片\n'
    '对我说 “sayo pixiv” 后传入图片'
)

permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser
@on_command('pixiv',aliases=('pa','pva','Pixiv'),permission=lambda sender:(not sender.is_privatechat) or sender.is_superuser )
async def _(session:CommandSession):
    pic = await session.aget(key='pic',prompt='请发出',at_sender=True,permission=permission)
    pic_date =Pixiv.m_ke(pic)
    totle = Pixiv.Pixivid_get(pic_date)
    r_all = f'''Name: {totle[1]}\nPixivID: {totle[0]}\nPixiv_url: {totle[2]}\n相似度： {totle[4]}\n{totle[3]}'''
    I_url = totle[3]
    await session.send("请稍后...")
    await session.send(f'''Name: {totle[1]}\nPixivID: {totle[0]}\nPixiv_url: {totle[2]}\n相似度： {totle[4]}\n'''+MessageSegment.image(I_url))




