import os
from dotenv import load_dotenv

load_dotenv()


class Headers:


    basic = {
        "Authorization": f"Bearer {os.getenv('TOKEN')}",
        "X-Task-Id": "API-1"
    }


print(Headers.basic)