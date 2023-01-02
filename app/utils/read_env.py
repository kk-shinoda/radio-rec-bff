import pathlib
import os
from dotenv import load_dotenv

def get_env(keys: list) -> dict:
    env = {}
    
    current_path = pathlib.Path(__file__).resolve().parent
    grand_parent_path = os.path.join('/'.join(str(current_path).split('/')[:-2]), '.env')
    load_dotenv(grand_parent_path)

    for key in keys:
        env.update({key: os.environ.get(key)})

    return env
