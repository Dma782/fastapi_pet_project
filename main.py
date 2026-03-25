from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, delete_table
from router import router as task_router
from fastapi.middleware.cors import CORSMiddleware


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
