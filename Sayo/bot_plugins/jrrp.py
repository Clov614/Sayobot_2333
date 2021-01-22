from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

from services.weather import get_current_weather_short, get_current_weather_desc
from services.common import ServiceException
from nonebot import message
import random

from bot import bot

__plugin_name__ = 'jrrp'
__plugin_usage__ = (
    '用法：\n'
    '对我说 “jrrp” 获取今日人品\n'
    'at我或者喊sayo 然后加上 jrrp\n'
    '例：sayo jrrp'

)


M_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser



@on_command('jrrp', aliases=('人品', '今日人品'), permission=M_permission)
async def _(session: CommandSession):
    rp = random.choice(range(0, 101))
    zf = random.choice(range(0,10))
    if zf == 0:
        await session.send(f'你今天的人品是：-{rp}',at_sender=True)
    else:
        mgs1 = await session.send(f'你今天的人品是：{rp}',at_sender=True)
        mgs2 = str(mgs1)

         # session.event.user_id, session.event.group_id
        U_id = session.event.user_id()

        await session.send(U_id)
