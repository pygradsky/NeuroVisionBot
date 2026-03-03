from dataclasses import dataclass


@dataclass
class BotMessages:
    start_message: str = (
        "👋 Привет!\n" 
        "Я бот, который умеет распознавать рукописные цифры на фото и изображениях. "
        "Просто отправь фото с цифрой или несколькими цифрами."
    )
