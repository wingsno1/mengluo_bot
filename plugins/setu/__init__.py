from nonebot import export, on_keyword, on_command
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment

from .data_source import get_pic_url

__zx_plugin_name__ = "色图"
__plugin_usage__ = f"""
usage：
    指令：
        色图: 随机色图
        色图 *[tags]: 在线搜索指定tag色图
    示例：色图 萝莉 猫娘
""".strip()
__plugin_des__ = "不要小看涩图啊混蛋！"
__plugin_cmd__ = ["色图 ?[tags]"]
__plugin_type__ = ("来点好康的",)
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["色图", "涩图", "setu", "色图 ?[tags]"],
}
__plugin_block_limit__ = {}
__plugin_cd_limit__ = {
    'rst': '您冲的太快了，请稍后再冲.',
}
<<<<<<< HEAD
__plugin_block_limit__ = {"rst": "你的色图正在路上，请稍等..."}
=======

>>>>>>> 3edbcbe... 第一个测试版

export = export()
export.description = '随机涩图'
export.usage = 'Usage:\n  setu/色图 [keyword]'
export.notice = ''
export.help = export.description + '\n' + export.usage + '\n' + export.notice

setu = on_keyword({'色图'}, priority=6)
setu_ = on_command('setu_', permission=SUPERUSER, priority=5)


@setu.handle()
async def _(bot: Bot, event: Event, state: T_State):
    key_word = str(event.get_message()).strip()
    words = ['setu', '涩图', '来份', '来张', '来个', '来点', '发份', '发张', '发个', '发点', '色图']
    for word in words:
        key_word = key_word.replace(word, '')
    img_url = await get_pic_url(key_word=key_word)
    if not img_url:
        await setu.finish('找不到相关的涩图')
    await setu.send(message=MessageSegment.image(file=img_url))
    await setu.finish()


@setu_.handle()
async def _(bot: Bot, event: Event, state: T_State):
    key_word = str(event.get_message()).replace('setu_', '').strip()
    img_url = await get_pic_url(key_word=key_word, r18=True)
    if not img_url:
        await setu_.finish('找不到相关的涩图')
    await setu_.send(message=MessageSegment.image(file=img_url))
    await setu_.finish()
