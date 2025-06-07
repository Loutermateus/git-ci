import os
from dotenv import load_dotenv

load_dotenv()


class Headers:


    basic = {
        "Authorization": f"Bearer {os.environ.get('TOKEN') or os.getenv('TOKEN')}",
        "X-Task-Id": "API-1"
    }


