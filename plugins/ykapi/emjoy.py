import requests
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
import random
from aiocqhttp import MessageSegment
import json

__zx_plugin_name__ = "表情包查找"
__plugin_usage__ = """
usage：
    搜索表情包
    指令：
        表情包查找 要查找的表情
""".strip()
__plugin_des__ = "搜索表情包"
__plugin_cmd__ = ["表情包"]
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["表情包查找"],
}

async def get_biao(text:str):
    url = ('https://api.iyk0.com/sbqb/?msg='+text)
    r = requests.get(url)
    result = json.loads(r.content)
    l = result['sum']
    k = random.randint(0, l)
    message = result['data_img'][k]['img']
    print(message)
    return message

BQB = on_command("表情包查找", priority=5)
@BQB.handle()
async def BQB_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
        if args:
            state["biao"] = args  # 如果用户发送了参数则直接赋值


@BQB.got("biao", prompt="你想查询神马表情包(@_@)...")
async def handle_biao(bot: Bot, event: Event, state: dict):
    biao = state["biao"]
    biaoqingbao = await get_biao(biao)
    await bot.send(
        event = event,
        message=MessageSegment.image(biaoqingbao)
    )