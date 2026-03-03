from aiogram import F, Router
from aiogram.types import Message

router = Router()


@router.message(F.photo)
async def photo_handler(message: Message) -> None:
    photo = message.photo[-1]
    await message.answer(
        "Photo received. Starting handwritten digits recognition.\n"
        f"File ID: {photo.file_id}"
    )
