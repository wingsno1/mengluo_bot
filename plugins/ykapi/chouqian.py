import requests
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
import json

__zx_plugin_name__ = "抽签"
__plugin_usage__ = """
usage：
    指令：
        抽签
""".strip()
__plugin_des__ = "抽签小游戏"
__plugin_cmd__ = ["抽签", "抛杯", "解签"]
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["抽签", "抛杯", "解签"],
}
# 抽签小游戏

async def get_chou(qq:str):
    url = 'https://api.iyk0.com/gdlq/?msg=抽签&n='+qq
    r = requests.get(url)
    message = r.text
    print(message)
    return message

CouQ = on_command("抽签", priority=5)
@CouQ.handle()
async def chouqian_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(await get_chou(str(Event.get_user_id))),
            at_sedner=True
        )
async def get_pao(qq:str):
    url = 'https://api.iyk0.com/gdlq/?msg=抛杯&n='+qq
    r = requests.get(url)
    message = r.text
    print(message)
    return message

PB = on_command("抛杯", priority=5)
@PB.handle()
async def paobei_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(await get_pao(str(Event.get_user_id))),
            at_sedner=True
        )
async def get_jie(qq:str):
    url = 'https://api.iyk0.com/gdlq/?msg=解签&n='+qq
    r = requests.get(url)
    result = json.loads(r.content)
    message = str(result['title']+'\n'+result['desc'])
    print(message)
    return message

PB = on_command("解签", priority=5)
@PB.handle()
async def paobei_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(await get_jie(str(Event.get_user_id))),
            at_sedner=True
        )