from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Создаем движок базы данных
DATABASE_URL = 'sqlite:///taskmanager.db'
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Создаем базовый класс для моделе
# Базовый класс для моделей
class Base(DeclarativeBase):
    pass