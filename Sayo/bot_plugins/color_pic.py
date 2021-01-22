from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment   # aiocqhttp 是 nonebot 的自带依赖

__plugin_name__ = '色图'
__plugin_usage__ = '用法： 对我说 “来份色图”'


img_url = 'http://fp1.fghrsh.net/2021/01/02/397dddbd846168a9ff30e51289ee7cdd.jpg'

@on_command('来份色图',aliases=('色图','laifensetu','setu'),permission=lambda sender:(not sender.is_privatechat) or sender.is_superuser )
async def _(session: CommandSession):
    await session.send(MessageSegment.image(img_url),at_sender=True)