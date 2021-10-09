import re
from .analysis_bilibili import b23_extract, bili_keyword
from nonebot import on_regex
from nonebot.adapters import Bot, Event

__zx_plugin_name__ = "哔哩哔哩视频解析"
__plugin_usage__ = """
usage：
    私聊或群聊自动转链接
""".strip()
__plugin_des__ = "哔哩哔哩解析"
__plugin_cmd__ = ["none"]
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["哔哩哔哩解析"],
}

analysis_bili = on_regex(r"(b23.tv)|(bili(22|23|33|2233).cn)|(live.bilibili.com)|(bilibili.com/(video|read|bangumi))|(^(av|cv)(\d+))|(^BV([a-zA-Z0-9])+)|(\[\[QQ小程序\]哔哩哔哩\])|(QQ小程序&amp;#93;哔哩哔哩)|(QQ小程序&#93;哔哩哔哩)", flags=re.I, priority=6)

@analysis_bili.handle()
async def analysis_main(bot: Bot, event: Event, state: dict):
    text = str(event.message).strip()
    if re.search(r"(b23.tv)|(bili(22|23|33|2233).cn)", text, re.I):
        # 提前处理短链接，避免解析到其他的
        text = await b23_extract(text)
    try:
        group_id = event.group_id
    except:
        group_id = "1"
    msg = await bili_keyword(group_id, text)
    if msg:
        msg = re.sub(r"简介.*", "", msg)
        await analysis_bili.send(msg)
