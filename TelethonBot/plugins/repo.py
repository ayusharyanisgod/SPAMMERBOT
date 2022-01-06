from .. import ATGK
from telethon import events, Button

@ATGK.on(events.NewMessage(incoming=True, pattern="/repo"))
async def repo(event):
    await event.reply("нєяє'ѕ ѕαя",
                    buttons=[
                        [Button.url("яєρο", url="https://t.me/AnonymusHu_Bot")],
                        [Button.url("sմթթօɾԵ gяουρ", url="https://t.me/AnonymusHu_Bot")]
                    ])
