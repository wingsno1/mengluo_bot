import requests
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
import json

__zx_plugin_name__ = "王者荣耀出装"
__plugin_usage__ = """
usage：
    搜王者出装和技巧玩法
    指令：
        王者荣耀出装 英雄名
""".strip()
__plugin_des__ = "搜王者出装和技巧玩法"
__plugin_cmd__ = ["王者荣耀"]
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["王者荣耀"],
}

async def get_wangzhe(text:str):
    url = ('https://api.iyk0.com/wzcz/?msg='+text)
    r = requests.get(url)
    result = json.loads(r.content)
    message = result['img']
    print(message)
    return message

# 王者荣耀出装
WZRY = on_command("王者荣耀出装", priority=4)
@WZRY.handle()
async def WZ_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
        if args:
            state["king"] = args  # 如果用户发送了参数则直接赋值


@WZRY.got("king", prompt="你想查询什么英雄(@_@)...")
async def handle_WZ(bot: Bot, event: Event, state: dict):
    king = state["king"]
    wangzhe = await get_wangzhe(king)
    await bot.send(
        event = event,
        message=MessageSegment.image(wangzhe)
    )