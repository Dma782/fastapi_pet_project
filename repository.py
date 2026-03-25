from database import async_session_builder, TasksORM
from schemas import STaskAdd, STask
from sqlalchemy import select


class TasksRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with async_session_builder() as session:
            task_dict = data.model_dump()
            task = TasksORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with async_session_builder() as session:
            query = select(TasksORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [
                STask.model_validate(task_model) for task_model in task_models
            ]
            return task_schemas
