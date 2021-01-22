from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment   # aiocqhttp 是 nonebot 的自带依赖
import requests
from services.picture_quest import picture_get
from bot import bot
import asyncio
import sources

__plugin_name__ = 'color_picture'
__plugin_usage__ = '用法： 对我说 “来份涩图”'

#@on_command修饰器 处理命令消息
@on_command('来份涩图',aliases=('涩图','img','setu'),permission=lambda sender:(not sender.is_privatechat) or sender.is_superuser )
async def _(session: CommandSession):
    img_url = picture_get()


    message = await session.send(img_url+MessageSegment.image(img_url),at_sender=True)

    messageID = message['message_id']
    await asyncio.sleep(30)  # 括号内的数字为撤回的秒数

    await bot.delete_msg(message_id=messageID)
