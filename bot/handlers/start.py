from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.resources.messages import BotMessages

bot_messages = BotMessages()
router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(bot_messages.start_message)
