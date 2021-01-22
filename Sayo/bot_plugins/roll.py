from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

from services.weather import get_current_weather_short, get_current_weather_desc
from services.common import ServiceException

import random

date_b = [0,1]
__plugin_name__ = 'roll'
__plugin_usage__ = (
    '用法：\n'
    '对我说 “sayo roll 内容1 内容2” 获取今日人品\n'
    '或者at我然后加上 roll 内容1 内容2\n'
)

obj = {
    1:"如果是我，我会选：",
    2:"当然是",
}

W_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser

@on_command('roll', aliases=('选择'), permission=W_permission)
async def _(session: CommandSession):
    args = session.current_arg_text.split(' ', 1)

    # if not args[0]:
    #     session.send('sayo不明白什么意思呢?')
    # if not args[1]:
    #     session.send('需要两段内容呢，注意空格隔开哦!!')
    #random模块为python的随机模块
    is_detailed = len(args) == 2
    rl = random.randint(0,1)
    obj_rl = random.randint(1,2)

    await session.send(f"{obj[obj_rl]}" + args[rl])

    if not is_detailed :
        session.send('需要两段内容呢，注意空格隔开哦!!')
    else:
        session.send(f"{obj[obj_rl]}"+args[rl])

