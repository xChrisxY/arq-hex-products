from sqlmodel import create_engine, Session, SQLModel, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import AsyncGenerator
from contextlib import asynccontextmanager
import os 

DATABASE_URL = os.getenv("DATABASE_URL", 'mysql+aiomysql://root:123456@localhost:3306/hexagonal_db"')

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

    def __new__(cls):
        if cls._instance is None: 
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
    
    def __init__(self): 
        self.engine = engine 
        self.AsyncSessionLocal = AsyncSessionLocal
        
    async def create_tables(self):
        try: 
            async with self.engine.begin() as conn: 
                await conn.run_sync(SQLModel.metadata.create_all)
            print("Conexión exitosa a la  base de datos y tablas creadas.")
        except Exception as error:
            print("Error al conectar con la base de datos o crear tablas: {error}")
            raise error 

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        # Obtener una sesión de base de datos asíncrona
        try:
            async with self.AsyncSessionLocal() as session: 
                yield session
        except Exception as error:
            print(f'Error al obtener la sesión_: {error}')
            raise error 
        
database = Database()        

@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async for session in database.get_session():
        yield session
    
    


