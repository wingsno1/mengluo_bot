import re
import datetime
from nonebot import export, on_command, on_endswith
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event

from .data_source import get_bangumi_info, get_new_bangumi

__zx_plugin_name__ = "番剧查询"
__plugin_usage__ = """
usage：
    更好的了解番剧
    指令：
        番剧查询: 番剧 {keyword}
        新番查询: 今日新番、明日新番、周几新番
""".strip()
__plugin_des__ = "查看新番，和搜索番剧"
__plugin_cmd__ = ["番剧", "今日新番", "明日新番", "周一新番", "周二新番", "周三新番", "周四新番", "周五新番", "周六新番", "周日新番"]
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["番剧查询"],
}

export = export()
export.description = '番剧查询'
export.usage = '用法:\n  1. 番剧查询: 番剧 {keyword}\n  2. 新番查询: 今日新番、明日新番、周几新番'
export.help = export.description + '\n' + export.usage

bangumi = on_command('番剧', priority=6)
bangumi_new = on_endswith('新番', priority=6)


@bangumi.handle()
async def _(bot: Bot, event: Event, state: T_State):
    keyword = str(event.get_message()).strip()
    if not keyword:
        await bangumi.finish(export.usage)

    msg = await get_bangumi_info(keyword)
    if not msg:
        await bangumi.finish('出错了，请稍后再试')

    await bangumi.send(message=msg)
    await bangumi.finish()


@bangumi_new.handle()
async def _(bot: Bot, event: Event, state: T_State):
    keyword = str(event.get_message()).strip().replace('新番', '')
    if not keyword:
        await bangumi_new.finish(export.usage)

    num = 1
    if keyword == '今日':
        day = 1
    elif keyword == '明日':
        day = 2
    else:
        match_obj = re.match(r'周(\S)', keyword)
        if match_obj:
            weeks = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '日': 7}
            week_raw = match_obj.group(1)
            if week_raw.isdigit() and 1 <= int(week_raw) <= 7:
                week = int(week_raw)
            elif week_raw in weeks:
                week = weeks[week_raw]
            else:
                await bangumi_new.finish('请输入正确的周数')
            week_now = int(datetime.datetime.now().weekday()) + 1
            day = 1
            while week_now != week:
                day += 1
                week_now += 1
                if week_now > 7:
                    week_now = 1
        else:
            await bangumi_new.finish()

    new_bangumi_list = await get_new_bangumi()
    if not new_bangumi_list:
        await bangumi_new.finish('出错了，请稍后再试')

    msg = new_bangumi_list[day - 1]
    await bangumi_new.send(message=msg)
    await bangumi_new.finish()
