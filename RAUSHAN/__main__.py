import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from RAUSHAN import LOGGER, app, userbot
from RAUSHAN.core.call import Anony
from RAUSHAN.misc import sudo
from RAUSHAN.plugins import ALL_MODULES
from RAUSHAN.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("RAUSHAN.plugins" + all_module)
    LOGGER("RAUSHAN.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://telegra.ph/file/e93428e2725f8c475c31d.mp4")
    except NoActiveGroupCall:
        LOGGER("RAUSHAN").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("RAUSHAN").info(
        "RERORT A BUG ON @fsyrl  , @Galerifsyrl FOR ANY ISSUES MADE BY FERDI"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("RAUSHAN").info("Stopping DEEP Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
