from functools import lru_cache
from pydantic import ValidationError
from pydantic_settings import BaseSettings  # Базовый класс для настроек

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN : str



    #JWT
    SECRET_KEY : str
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    CORS_ORIGINS : list = ['http://localhost:3000']
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    try:
        return Settings()
    except ValidationError as e:
        print(f"Ошибка загрузки настроек: {e}")
        # Возвращаем дефолтные настройки или завершаем работу
        exit(1)

settings = get_settings()