from .init_group_manager import init_group_manager, group_manager
from .init_plugins_config import init_plugins_config
from .init_plugins_data import init_plugins_data, plugins_manager
from .init_none_plugin_count_manager import init_none_plugin_count_manager
from .init_plugins_resources import init_plugins_resources
from .init_plugins_settings import init_plugins_settings
from .init_plugins_limit import (
    init_plugins_block_limit,
    init_plugins_count_limit,
    init_plugins_cd_limit,
)
from .check_plugin_status import check_plugin_status
from nonebot.adapters.cqhttp import Bot
from configs.path_config import DATA_PATH
from services.log import logger
from nonebot import Driver
import nonebot


__zx_plugin_name__ = "初始化插件数据 [Hidden]"
__plugin_version__ = 0.1
__plugin_author__ = "HibiKier"


driver: Driver = nonebot.get_driver()


@driver.on_startup
def _():
    """
    初始化数据
    """
    init_plugins_settings(DATA_PATH)
    init_plugins_cd_limit(DATA_PATH)
    init_plugins_block_limit(DATA_PATH)
    init_plugins_count_limit(DATA_PATH)
    init_plugins_data(DATA_PATH)
    init_plugins_config(DATA_PATH)
    init_plugins_resources()
    init_none_plugin_count_manager()
    x = group_manager.get_super_old_data()
    if x:
        for key in x.keys():
            plugins_manager.block_plugin(key, block_type=x[key])
    logger.info("初始化数据完成...")


@driver.on_bot_connect
async def _(bot: Bot):
    await init_group_manager()
    await check_plugin_status(bot)
