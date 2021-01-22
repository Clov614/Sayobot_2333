from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

from services.Up_kebiao import KB
from aiocqhttp.message import MessageSegment

__plugin_name__ = '课表'
__plugin_usage__ = (
    '用法：\n'
    '对我说 “课表” 调出课表\n'
    '对我说 ”存课表“ 手动将课表存入'
)

permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser
@on_command('存张课表',aliases=('存课表','给你课表'))
async def _(session:CommandSession):
    pic = await session.aget(key='pic',prompt='请发出',at_sender = True,permission=permission)
    pic_date =KB.m_ke(pic)

    await session.send("保存成功!!")

    await session.send(pic_date)


@on_command('课表', aliases=('给我课表'),permission=permission)
async def _(session:CommandSession):
    image_url = KB.url_output('课表')
    await session.send(image_url)

@on_command('删课表', aliases=('删除课表'),permission=permission)
async def _(session:CommandSession):
    KB.del_KeBiao(None)
    await session.send('删除成功')







