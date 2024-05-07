from fastapi import APIRouter
from schemas import STaskAdd, STask, STaskID
from typing_extensions import Annotated
from fastapi.params import Depends
from repository import TaskRepository

router = APIRouter(
    prefix='/tasks',
    tags=['Таски']
)

@router.post('')
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get('')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks