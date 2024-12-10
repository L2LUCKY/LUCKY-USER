import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", "25609334"))
API_HASH = getenv("API_HASH", "ad0ff353206ea1ebce1ab8bfca9f3f7b")
BOT_TOKEN = getenv("BOT_TOKEN", "6541753178:AAGMpOcmo8KvLQ7yviurPAiPSu7BOgHlnlA")
STRING_SESSION = getenv("STRING_SESSION", "BQGt9tsAlUezTyE3NXPzgyhZ58zkS8IcG2bdCq2IM43OBYqIWQe2FvASn0w-spivpvcLyjvxFhKQWdCL_gcK_XTu_41izKR21kd48DpRKt36AaHdxdf1RB6P54MhVWNMCaGvAwqdU9UMajcdl-j95zPZ42gOvaehq-MEI-1gUeKcd_fpSis5IO4MiPsJpQTtdphra9SDVqd1afc5fneiczrIQ3MHX21EZVT3-HEc2o0NumIpYjuTKmaVGTShMPtRaJHkos-f3mudmUQTvD8xmqCrrctYJglEQr3zxektJ0DYYcjfj_wNYwP_CmgQuMO98010gbbSmOF1WxKZMpCly0teia2YBwAAAAFC8M17AA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Chiku12:Chiku12@arman.wsumgkn.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001963452122"))



SESSION_STRING = getenv("SESSION_STRING", "BQGt9tsANPWXfgm6seuXcc3Vwj-r6uhrPIjL3dToZI3lyMAJ8W8TKHd4dw-D88q-D5dgdHQJ4TtgIvqAeedLzISgwShIITqWfzRTHB-2g2Q2PS8sFW1AGgveVjOqkmHpnB2Se6H0uaicTrntpUo-6lfvClazwKejA_Us-OKnEi0eXl7xL_MYOk8QK8XNfOMz-5cDqhiDKVpqpM68ojxYoHh3Tt5Ou8PqOYzn2A2gjLjYX1KrwHvupFxZ-KTWQhNshehU7DXwOlEUfIDUSXfvJHyGFPYPg-cgvkFeWAiRncnwO96LTvOAMMjHlKE0IPU1EiYDSL_lYKEtue4GWKLwHrHcxNfKyQAAAAFC8M17AA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())




PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**Hᴇʏ ᴛʜᴇʀᴇ! I'ᴍ ᴀ ʀᴇᴀʟʟʏ sᴍᴀʀᴛ ᴀɴᴅ ғᴀsᴛ ᴀssɪsᴛᴀɴᴛ ʙᴏᴛ ᴡɪᴛʜ ᴛᴏᴘ-ɴᴏᴛᴄʜ sᴇᴄᴜʀɪᴛʏ.\n I ᴡᴏɴ'ᴛ ʟᴇᴛ ʏᴏᴜ ᴍᴇssᴀɢᴇ ᴍʏ ᴏᴡɴᴇʀ ᴅɪʀᴇᴄᴛʟʏ ᴜɴʟᴇss ᴛʜᴇʏ sᴀʏ ɪᴛ's ᴏᴋᴀʏ. Rɪɢʜᴛ ɴᴏᴡ, ᴍʏ ᴏᴡɴᴇʀ ɪsɴ'ᴛ ᴏɴʟɪɴᴇ, sᴏ ʏᴏᴜ'ʟʟ ʜᴀᴠᴇ ᴛᴏ ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴛʜᴇʏ ɢɪᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ. Aɴᴅ ᴘʟᴇᴀsᴇ, ᴅᴏɴ'ᴛ sᴘᴀᴍ ʜᴇʀᴇ – ɪғ ʏᴏᴜ ᴅᴏ,\n\n I ᴍɪɢʜᴛ ʜᴀᴠᴇ ᴛᴏ ʙʟᴏᴄᴋ ʏᴏᴜ ғʀᴏᴍ ᴄᴏɴᴛᴀᴄᴛɪɴɢ ᴍʏ ᴏᴡɴᴇʀ.**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://te.legra.ph/file/6926207a8c9c4b8e4b93c.jpg")



LOGGER = logging.getLogger("DIL")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = [5247304559]


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

