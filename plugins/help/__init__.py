from nonebot import on_command
from nonebot.adapters.cqhttp import (
    Bot,
    MessageEvent,
)
from nonebot.typing import T_State
from configs.path_config import IMAGE_PATH
from utils.message_builder import image
from .data_source import create_help_img, get_plugin_help
from utils.utils import get_message_text
from pathlib import Path


__zx_plugin_name__ = "帮助"


help_image = Path(IMAGE_PATH) / "help.png"
simple_help_image = Path(IMAGE_PATH) / "simple_help.png"
if help_image.exists():
    help_image.unlink()
if simple_help_image.exists():
    simple_help_image.unlink()

_help = on_command("详细功能", aliases={"详细帮助", "详细菜单"}, priority=1, block=True)
simple_help = on_command("功能", aliases={"help", "帮助", "菜单"}, priority=1, block=True)


@_help.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    if not help_image.exists():
        if help_image.exists():
            help_image.unlink()
        if simple_help_image.exists():
            simple_help_image.unlink()
        await create_help_img(help_image, simple_help_image)
    await _help.finish(image("help.png"))


@simple_help.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    msg = get_message_text(event.json())
    is_super = False
    if msg:
        if '-super' in msg:
            if str(event.user_id) in bot.config.superusers:
                is_super = True
            msg = msg.replace('-super', '')
        msg = get_plugin_help(msg, is_super)
        if msg:
            await _help.send(image(b64=msg))
        else:
            await _help.send("没有此功能的帮助信息...")
    else:
        if not simple_help_image.exists():
            if help_image.exists():
                help_image.unlink()
            if simple_help_image.exists():
                simple_help_image.unlink()
            await create_help_img(help_image, simple_help_image)
        await _help.finish(image("simple_help.png"))
