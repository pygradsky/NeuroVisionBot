import os

from aiogram import F, Router
from aiogram.types import Message

from bot.configs.config import Data
from bot.resources.messages import BotMessages

router = Router()
bot_messages = BotMessages()
data = Data()


@router.message(F.photo)
async def photo_handler(message: Message) -> None:
    user_id = message.from_user.id if message.from_user else ""
    if not user_id:
        await message.answer(bot_messages.none_user_id)
        return

    try:
        photos_dir = os.path.join(data.downloads_dir, str(user_id), "photos")
        os.makedirs(photos_dir, exist_ok=True)

        photo = message.photo[-1]
        filename = f"photo.jpg"
        photo_path = os.path.join(photos_dir, filename)

        await message.bot.download(photo, destination=photo_path)
        await message.answer(bot_messages.downloaded_photo)
    except (FileNotFoundError, OSError):
        await message.answer(bot_messages.failed_to_download_photo)
