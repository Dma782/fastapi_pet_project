from fastapi import APIRouter, Depends
from schemas import STaskAdd, STask, STaskUpdate
from repository import TasksRepository


router = APIRouter(prefix="/tasks")


@router.post("/add")
async def add_task(task: STaskAdd):
    task_id = await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("/get")
async def get_home() -> list[STask]:
    tasks = await TasksRepository.find_all()
    return tasks


@router.post("/update")
async def update_task(task: STaskUpdate):
    task_id = await TasksRepository.update(task)
    return {"ok": True, "task_id": task_id}
