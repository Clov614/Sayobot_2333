from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

from services.get_BQB import bqb_url

import re
import requests
import base64

__plugin_name__ = '表情包'
__plugin_usage__ = (
    '用法：\n'
    '对我说 “表情包” \n'
    '或者对我说 “bqb”'
)
permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser

@on_command('bqb', aliases=('表情包', 'Bqb'), permission=permission)
async def _(session: CommandSession):

    args = session.current_arg_text.strip().split(' ', 1)

    if not args[0]:
        args[0] = 3
    j = int(args[0]) - 1
    href, target, = bqb_url(args[0])
    total1 = f'{href[0]}[CQ:image,file={target[0]}]'
    for i in range(0,j):
        headers = {
            'Referer':href[i]
        }
        text = requests.get(url=target[i],headers=headers).text
        text = text.encode('utf-8')
        new = base64.b64encode(text)
        total = f'''[CQ:image,file={new}]'''
        await session.send(total)
