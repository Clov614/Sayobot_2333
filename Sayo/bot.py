from os import path

import nonebot
import bot_config
from bot_plugins.blibli_get import get_msg

nonebot.init(bot_config)
# 第一个参数为插件路径，第二个参数为插件前缀（模块的前缀）
nonebot.load_plugins(path.join(path.dirname(__file__), 'bot_plugins'), 'bot_plugins')

# 如果使用 asgi
bot = nonebot.get_bot()
app = bot.asgi

# @bot.on_message()  #监听所有消息
# async def handle_group_message(ctx):
#     # print("group ctx>>",ctx)
#     with open("./sources/msg.db",'w',encoding='utf-8') as fp:
#         fp.write(str(ctx))
#         fp.close()
#         get_msg()
#     return ctx


if __name__ == '__main__':
    nonebot.run()
    # get_msg()
