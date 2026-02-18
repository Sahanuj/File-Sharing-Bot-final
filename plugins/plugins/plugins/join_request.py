#(©)CodeXBotz

from pyrogram.types import ChatJoinRequest

from bot import Bot
from database.database import add_join_request


@Bot.on_chat_join_request()
async def track_join_request(client, join_request: ChatJoinRequest):
    await add_join_request(join_request.chat.id, join_request.from_user.id)
    if join_request.chat.username:
        await add_join_request(f"@{join_request.chat.username.lower()}", join_request.from_user.id)
