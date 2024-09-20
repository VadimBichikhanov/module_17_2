from backend.db import engine, Base
from models.user import User
from models.task import Task
from sqlalchemy.schema import CreateTable

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

# Выводим SQL-запрос для создания таблиц

print(CreateTable(User.__table__).compile(engine))
print(CreateTable(Task.__table__).compile(engine))
