from nonebot import export, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event

from .data_source import get_steam_game

__zx_plugin_name__ = "steam游戏查询"
__plugin_usage__ = """
usage：
    普普通通的查天气吧
    指令：
       steam {keyword}
""".strip()
__plugin_des__ = "查查看steam的游戏"
__plugin_cmd__ = ["steam [游戏]"]
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["steam"],
}

export = export()
export.description = 'Steam游戏查询'
export.usage = 'Usage:\n  steam {keyword}'
export.help = export.description + '\n' + export.usage

steam = on_command('steam', priority=5)


@steam.handle()
async def _(bot: Bot, event: Event, state: T_State):
    keyword = str(event.get_message()).strip()
    if not keyword:
        await steam.finish(export.usage)

    msg = await get_steam_game(keyword)
    if not msg:
        await steam.finish('出错了，请稍后再试')

    await steam.send(message=msg)
    await steam.finish()
