from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

#整点报时，group_id为报时的群号
@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=672076603,
                                 message=f'洋河蓝色经典提醒您，现在是北京时间{now.hour}点整！')
    except CQHttpError:
        pass


# 现在{now.hour}点整啦！