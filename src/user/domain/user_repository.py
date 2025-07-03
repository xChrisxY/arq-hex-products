from abc import ABC, abstractmethod
from typing import List, Optional 
from .user import User

class IUserRepository(ABC):
    
    @abstractmethod
    async def create(self, user: User) -> User: 
        pass 
    
    @abstractmethod 
    async def get_by_email(self, email: str) -> Optional[User]: 
        pass 
    
    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[User]: 
        pass

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        pass
    
    
