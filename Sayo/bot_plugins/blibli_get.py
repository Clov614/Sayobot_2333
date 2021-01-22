#coding=utf-8
import re
from services.blibli_analysis import blibli_get
import time
from nonebot import message_preprocessor, session



# async def _(session :NLPSession):
#     T_session = session.msg_text
#     await session.send(T_session)
#
# _(session=)



# @message_preprocessor
# async def _(bot, event, manager):
#     msg = await listen_to_broadcasts()
#     NLPSession.send(msg)
#
# _()

# _counts = [0 for _ in range(61)]
#
# _epoch = datetime.now()
#
# def _get_offset() -> int:
#     return int((datetime.now() - _epoch).total_seconds()) % 61
#
#
# async def get_count(curr_s: Optional[int] = None) -> Dict[str, int]:
#     'Gets report that counts number of messages received in last 60s and last second.'
#     if curr_s is None:
#         curr_s = _get_offset()
#     return {
#         'lastMin': sum(_counts),
#         'lastSec': _counts[curr_s - 1], # note [-1] indexes to [60]!
#     }

# handle_group_message()
ex = r'qqdocurl":"(.*?)\?'
def get_msg():
    session.send("111")
    while True:
        with open("./sources/msg.db",'r',encoding='utf-8') as fp:
            msg_m = fp.read()
            fp.close()

            msg_d = re.findall(ex,msg_m)
        if msg_d != None:
            msg_date = msg_d[0]
            total_all = blibli_get(msg_date)
            session.send(total_all[0])
        session.send(total_all[1])

        time.sleep(0.5)











