import json
import nonebot
import requests
from configs.config import GROUP_TIMEREPO
from aiocqhttp import MessageSegment
from nonebot import require

group_id_list=GROUP_TIMEREPO

scheduler = require('nonebot_plugin_apscheduler').scheduler

def get_zaobao():
    url = 'https://api.iyk0.com/60s'
    r = requests.get(url)
    result = json.loads(r.content)
    message = result['imageUrl']
    return message
def get_today():
    url='https://api.iyk0.com/jr/'
    r = requests.get(url)
    result = json.loads(r.content)
    message = str(result['surplus'])
    return message

@scheduler.scheduled_job('cron', hour='8',minute='00', id='zaobao')
async def zaobao():
    (bot,) = nonebot.get_bots().values()
    text = get_zaobao()
    text.replace('\n', '')
    for id in group_id_list:
        await bot.send_msg(
            message_type="group",
            group_id=int(id),
            message='早上好呀☀\n━━━━━━━━\n60s读懂世界\n'+MessageSegment.image(text)
        )
        await bot.send_msg(
            message_type="group",
            group_id=int(id),
            message=str(get_today())
        )

