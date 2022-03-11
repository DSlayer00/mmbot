import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class ENV_VARS(object):
    API_ID = int(os.environ.get("1190894"))
    API_HASH = os.environ.get("e8b74a7639f9b4787b1916acbe43f74d")
    BIFM_URL = os.environ.get("BIFM_URL", "https://bifm.tacohitbox.com/api/bypass?url")
    BOT_TOKEN = os.environ.get("5146101918:AAH7gJ90NW7Rgml5iU1JBBI5gjXERbDSmJE")
    BOT_USERNAME = os.environ.get("bypasserobot")
    LANGUAGE = os.environ.get("LANGUAGE", "EN")

Config = ENV_VARS

handler = Config.BOT_USERNAME
class CMD(object):
    START = ["start", f"start@{handler}"]
    ATSN = ["artstation", f"artstation@{handler}"]
    BIFM = ["bifm", f"bifm@{handler}"]
    DPLK = ["droplink", f"droplink@{handler}"]
    GPLK = ["gplink", f"gplink@{handler}"]
    MDIK = ["mdisk", f"mdisk@{handler}"]
    OUOK = ["ouo", f"ouo@{handler}"]
    WETR = ["wetransfer", f"wetransfer@{handler}"]
