import os
import random
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, MessageEvent
from nonebot.typing import T_State
from utils.message_builder import record
from configs.path_config import VOICE_PATH

__zx_plugin_name__ = "原神KFC语音"
__plugin_usage__ = """
usage：
    （异世相遇，尽享美味！）
    在QQ群发送指定的指令，Bot会随机选择一条语音回复
    指令：
        KFC/kfc/原神KFC/原神kfc/二次元KFC/二次元kfc/异世相遇尽享美味
""".strip()
__plugin_des__ = "原神KFC语音插件（呐呐呐，服务员欧尼酱~~......异世相遇，尽享美味！）"
__plugin_cmd__ = ["KFC/kfc/原神KFC/原神kfc/二次元KFC/二次元kfc/异世相遇尽享美味"]
__plugin_type__ = ("原神相关",)
__plugin_version__ = 0.1
__plugin_author__ = "梦璃雨落"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["KFC", "kfc", "原神KFC", "原神kfc", "二次元KFC", "二次元kfc", "异世相遇尽享美味"],
}


sv = on_command('KFC', aliases={'kfc', '原神KFC', '原神kfc', '二次元KFC', '二次元kfc', '异世相遇尽享美味'}, priority=5, block=True)





@sv.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        voice = random.choice(os.listdir(VOICE_PATH + "record/"))
        result = record(voice, "record")
        await sv.send(result)
    except:
        await sv.send("发送失败")
