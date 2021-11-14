import json
import requests
from nonebot import on_command
from nonebot.typing import T_State
from utils.utils import get_message_text
from nonebot import require
from nonebot.adapters.cqhttp import Bot, MessageEvent

__zx_plugin_name__ = "网站工具"
__plugin_usage__ = """
usage：
    网站基础查询工具
    指令：
        ping [网址]]        查看网站延迟/IP信息
        页面信息信息 [网址]   查看页面信息，介绍
        搜索引擎收录 [网址]   查看网站收录情况
        备案查询  [网址]     查看网站备案
""".strip()
__plugin_des__ = "网址基础工具"
__plugin_cmd__ = ["ping", "页面信息信息", "搜索引擎收录", "备案查询"]
__plugin_type__ = ("一些工具",)
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["网站工具"],
}

Ping = on_command("ping", priority=5, block=True)

@Ping.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    msg = get_message_text(event.json())
    if msg:
        url = 'https://api.iyk0.com/ping/?url=%s'%(msg)
        r = requests.get(url)
        message = r.text
        await Ping.send(message)
    else:
        message = "请输入查询域名"
        await Ping.send(message)

Webinfo = on_command("页面信息", priority=5, block=True)

@Webinfo.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    msg = get_message_text(event.json())
    if msg:
        url = 'https://api.iyk0.com/wzbt/?url=%s'%(msg)
        r = requests.get(url)
        result = json.loads(r.content)
        Title = result['title']
        Site = result['site']
        Keywords = result['keywords']
        Description = result['description']
        message = "梦落页面信息查询： \n网站： %s \n网站标题： %s \n关键词： %s \n简介： %s"%(Site,Title,Keywords,Description)
        await Webinfo.send(message)
    else:
        message = "请输入查询域名"
        await Webinfo.send(message)

Shou = on_command("搜索引擎收录", priority=5, block=True)

@Shou.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    msg = get_message_text(event.json())
    if msg:
        url = 'https://api.iyk0.com/shou/?url=%s'%(msg)
        r = requests.get(url)
        result = json.loads(r.content)
        Site = result['data']['url']
        Baidu = result['data']['baidu']
        Haoso = result['data']['haoso']
        Sogou = result['data']['sogou']
        message = "梦落搜索引擎收录查询： \n网站： %s \n百度搜索收录量： %s \n360搜索收录量： %s \n搜狗搜索收录量： %s"%(Site,Baidu,Haoso,Sogou)
        await Shou.send(message)
    else:
        message = "请输入查询域名"
        await Shou.send(message)

Icp = on_command("备案查询", priority=5, block=True)

@Icp.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    msg = get_message_text(event.json())
    if msg:
        url = 'https://api.iyk0.com/beian/?url=%s'%(msg)
        r = requests.get(url)
        result = json.loads(r.content)
        Flag = result['msg']
        if Flag == "查询成功!":
            Name = result['name']
            Siteindex = result['siteindex']
            Nature = result['nature']
            icp = result['icp']
            Sitename = result['sitename']
            Time = result['time']
            message = "梦落备案查询： \n网站名称： %s \n域名： %s \n备案/许可证号： %s \n主办单位名称： %s \n主办单位性质： %s\n审核通过日期： %s"%(Sitename,Siteindex,icp,Name,Nature,Time)
            await Icp.send(message)
        else:
            message = "该网站未备案"
            await Icp.send(message)
    else:
        message = "请输入查询域名"
        await Icp.send(message)
