from sqlmodel import create_engine, Session, SQLModel, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker
from typing import AsyncGenerator
import os 

from .entities.product_entity import ProductEntity

DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el engine asíncrono
engine = create_async_engine(DATABASE_URL, echo=False, pool_recycle=3600)

# Crear SessionLocal asíncrona
AsyncSessionLocal = async_sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

class Database:
    _instance = None 
    
    


