from fastapi import APIRouter, Depends
from schemas import STaskAdd, STask
from typing import Annotated
from repository import TasksRepository


router = APIRouter(prefix="/tasks")


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    task_id = await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_home() -> list[STask]:
    tasks = await TasksRepository.find_all()
    return tasks
