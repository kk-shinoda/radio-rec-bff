import requests
import json
from .read_env import get_env
from logging import getLogger

header = {"Content-Type": "application/json"}
logger = getLogger('uvicorn')

def post_line(data: dict):
    logger.info('start post line')
    data = {"from": "radio-rec-bff", **data}
    url = get_env(["LINE_BOT_URL"])["LINE_BOT_URL"]
    res = requests.post(
        headers=header,
        url=url,
        data=json.dumps(data)
    )
    logger.info(res)
