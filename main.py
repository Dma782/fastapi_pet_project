from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, delete_table
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print("база очищена")
    await create_table()
    print("база готова к роботе")
    yield
    print("выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
