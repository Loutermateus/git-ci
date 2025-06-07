

import os

raw_stage = os.environ.get("STAGE", "").lower()

if raw_stage == "dev":
    STAGE = "https://dev-gs.qa-playground.com/api/v1"
elif raw_stage == "release":
    STAGE = "https://release-gs.qa-playground.com/api/v1"
else:
    raise ValueError(f"Unknown STAGE: {raw_stage!r}")


class Endpoints:


    list_all_users = f"{STAGE}/users"
    delete_user_by_id  = lambda self, user_id: f"{STAGE}/users/{user_id}"
    create_user = f"{STAGE}/users"
