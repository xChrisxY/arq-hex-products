from fastapi import FastAPI 
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from product.infraestructure.routers.product_router import router as product_router
from database.mysql import database

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.create_tables()
    yield

app = FastAPI(title="Hexagonal Architecture API", description="Una API simple Arquitectura Hexagonal con FastAPI", version="1.0.0", lifespan=lifespan)

app.add_middleware(CORSMiddleware, allow_origins = ["*"], allow_credentials = True, allow_methods = ["*"], allow_headers = ["*"])

app.include_router(product_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}


if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8000)

