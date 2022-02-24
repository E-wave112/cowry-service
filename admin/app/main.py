from fastapi import FastAPI
from app.api.admin import admins
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/admins/openapi.json", docs_url="/api/v1/admins/docs")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(admins, prefix="/api/v1/admins", tags=["admins"])
