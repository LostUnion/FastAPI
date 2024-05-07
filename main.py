from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from pprint import pprint

from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    pprint("База очищена")
    await create_tables()
    pprint("База готова к работе")
    yield
    pprint("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)



