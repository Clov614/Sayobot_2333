from nonebot.natural_language import NLPSession, IntentCommand
from nonebot.experimental.plugin import on_command, on_natural_language
from nonebot.command import CommandSession
from jieba import posseg


w_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser

new = "大佐是谁，哦~爬！！！"
@on_command('大佐', aliases=('恶心心', '培桑','大作','培培'), permission=w_permission)
async def _(session: CommandSession):
    await session.send(new)

@on_command('大佐不能爬', aliases=('培培'), permission=w_permission)
async def _(session: CommandSession):
    await session.send('大佐不能爬！！！')

@on_natural_language(keywords={'二次元'}, permission=w_permission)
async def _(session: NLPSession):
    # 使用 jieba 将消息句子分词
    words = posseg.lcut(session.msg_text.strip())


    for word in words:
        if word in ('能不能','爬'):
            new = "二次元不能爬，大佐才喜欢爬呢！"


    return IntentCommand(60, '大佐不能爬')
