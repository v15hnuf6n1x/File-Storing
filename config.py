import os

API_ID = int(os.environ.get("21165589", 0))
API_HASH = os.environ.get("8cc762f4873e84a7cf0cbfd66a07244b")
BOT_TOKEN = os.environ.get("B6517235191:AAF0A550ymSnlbPyNJvf7otys0v6mwuluWk")
DB_CHANNEL_ID = os.environ.get("-1001869648454")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("2048030675")
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
