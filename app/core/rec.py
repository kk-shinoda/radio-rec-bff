from utils.read_env import get_env
from utils.get_recent_date import get_recent_date
from utils.upload_gdrive import upload
from utils.post_line import post_line
import subprocess
from typing import NamedTuple
from logging import getLogger
import os

class RecInfo(NamedTuple):
    title: str
    station: str
    date: str
    start_time: str
    duration: str
    folder_id: str

def rec(info: dict):
    logger = getLogger('uvicorn')
    env = get_env(["COMMAND", "ARCHIVE_DIR", "MAIL", "PASSWORD"])
    rec_info = RecInfo(**info)
    date = get_recent_date(int(rec_info.date))
    start_datetime = date + rec_info.start_time
    
    file_name = f"{date}_{rec_info.title}"
    output = f"{env['ARCHIVE_DIR']}/{rec_info.title}/{file_name}.m4a"
    logger.info(f'rec start {output}')

    os.makedirs(f"{env['ARCHIVE_DIR']}/{rec_info.title}", exist_ok=True)

    subprocess.run([f"{env['COMMAND']} \
                    -s {rec_info.station} \
                    -f {start_datetime} \
                    -d {rec_info.duration} \
                    -o {output} \
                    -m {env['MAIL']} \
                    -p {env['PASSWORD']}"],
                    shell=True)

    logger.info('rec done')
    file_id = upload(output, rec_info.folder_id)
    post_line({"file_id": file_id, "file_name": file_name})
