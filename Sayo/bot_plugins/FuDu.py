from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command


__plugin_name__ = '复读'
__plugin_usage__ = (
    '用法：\n'
    '对我说 复读 复读的内容\n'
    '或者 echo 复读的内容'
)

weather_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser

@on_command('echo', aliases=('复读'),permission=weather_permission)
async def _(session: CommandSession):
    await session.send(session.current_arg)