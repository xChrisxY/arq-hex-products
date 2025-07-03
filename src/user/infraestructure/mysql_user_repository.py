from ..domain.user import User
from ..domain.user_repository import IUserRepository

from database.mysql import get_db_session
from database.entities.user_entity import UserEntity


from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from typing import Optional

class MySQLUserRepository(IUserRepository):
    
    def __init__(self):
        self.get_db = get_db_session
        
    async def create(self, user: User) -> User:
        
        async with self.get_db() as db_session:
            
            try: 
                
                user_entity = UserEntity(
                    username=user.username, 
                    email=user.email,
                    password_hash=user.password_hash
                )
                
                db_session.add(user_entity)
                await db_session.commit()
                await db_session.refresh(user_entity)
                
                # Convertir la entidad a modelo de dominio
                domain_user = User(
                    id=user_entity.id,
                    username=user_entity.username, 
                    email=user_entity.email, 
                    password_hash=user_entity.password_hash, 
                    created_at=user_entity.created_at, 
                    updated_at=user_entity.updated_at
                )

                return domain_user
            
            except IntegrityError as e: 
                await db_session.rollback()
                raise ValueError(f'Error de integridad al crear el usuario: {e}')
            
            except Exception as error: 
                await db_session.rollback()
                print(f'Error al crear el usuario: {error}')
                raise error 

                
    async def get_by_email(self, email: str) -> Optional[User]:

        async with self.get_db() as db_session:
            
            try: 
                
                statement = select(UserEntity).where(UserEntity.email == email.strip().lower())
                results = await db_session.exec(statement)
                user_entity = results.first()
                
                if not user_entity:
                    return None 
                
                domain_user = User(
                    id=user_entity.id,
                    username=user_entity.username, 
                    email=user_entity.email, 
                    password_hash=user_entity.password_hash, 
                    created_at=user_entity.created_at, 
                    updated_at=user_entity.updated_at
                )

                return domain_user
            
            except Exception as error: 
                await db_session.rollback()
                print(f'Error al obtener el usuario: {error}')
                raise error 

                
    async def get_by_username(self, username: str) -> Optional[User]:
        
        async with self.get_db() as db_session: 
            
            try: 
                
                statement = select(UserEntity).where(UserEntity.username == username)
                results = await db_session.exec(statement)
                user_entity = results.first()
                
                if not user_entity:
                    return None 
                
                domain_user = User(
                    id=user_entity.id,
                    username=user_entity.username, 
                    email=user_entity.email, 
                    password_hash=user_entity.password_hash, 
                    created_at=user_entity.created_at, 
                    updated_at=user_entity.updated_at
                )

                return domain_user
                
            except Exception as error: 
                await db_session.rollback()
                print(f'Error al obtener el usuario: {error}')
                raise error 

    async def get_by_id(self, user_id: int) -> Optional[User]:
        
        async with self.get_db() as db_session: 
            
            try: 
                
                statement = select(UserEntity).where(UserEntity.id == user_id)
                results = await db_session.exec(statement)
                user_entity = results.first()
                
                if not user_entity:
                    return None 
                
                domain_user = User(
                    id=user_entity.id,
                    username=user_entity.username, 
                    email=user_entity.email, 
                    password_hash=user_entity.password_hash, 
                    created_at=user_entity.created_at, 
                    updated_at=user_entity.updated_at
                )

                return domain_user
                
            except Exception as error: 
                await db_session.rollback()
                print(f'Error al obtener el usuario: {error}')
                raise error 
