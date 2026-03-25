from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "pet_project"

    def DATABASE_URL_psycopg(self):
        # postgresql+psycopg://postgres:Rth@Dc6ECy5v4tE@localhost:5432/fast_api
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    def DATABASE_URL_asyncpg(self):
        # postgresql+psycopg://postgres:Rth@Dc6ECy5v4tE@localhost:5432/fast_api
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()

engine = create_engine(url=settings.DATABASE_URL_psycopg())
async_engine = create_async_engine(url=settings.DATABASE_URL_asyncpg())

session_builder = sessionmaker(engine)
async_session_builder = async_sessionmaker(async_engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TasksORM(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]


async def create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
