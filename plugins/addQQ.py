from nonebot import on_request
from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import FriendRequestEvent,FriendAddNoticeEvent

__zx_plugin_name__ = "默认消息"
__plugin_usage__ = """
usage：
    添加好友后自动触发
""".strip()
__plugin_des__ = "默认消息"
__plugin_type__ = ("被动相关",)
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"

add = on_request()
@add.handle()
async def add_(bot:Bot,event:FriendRequestEvent):
    await event.approve(bot)


msgadd = on_notice()
@msgadd.handle()
async def sendmsg_(bot:Bot,event:FriendAddNoticeEvent):
    await bot.send(
        event=event,
        message='请输入帮助，然后和我一起玩叭',
    )
