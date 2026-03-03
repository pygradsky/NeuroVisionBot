from dataclasses import dataclass


@dataclass
class BotMessages:
    start_message: str = (
        "👋 Привет!\n" 
        "Я бот, который умеет распознавать рукописные цифры на фото и изображениях. "
        "Просто отправь фото с цифрой или несколькими цифрами."
    )
    downloaded_photo: str = (
        "✅ Фото сохранено, начинаю распознавание."
    )
    failed_to_download_photo: str = (
        "❌ Возникла ошибка при сохранении фотографии."
    )
    none_user_id: str = (
        "❌ Не удалось определить ваш ID."
    )
