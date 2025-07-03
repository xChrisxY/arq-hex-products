from typing import Optional
from ...domain.user import User
from ...domain.user_repository import IUserRepository
from ...application.services.encrypt_service import IEncryptService 

class AuthServiceUseCase: 
    
    def __init__(self, user_repository: IUserRepository, encrypt_service: IEncryptService):
        self.user_repository = user_repository 
        self.encrypt_service = encrypt_service 
        
    async def execute(self, email: str, password: str) -> Optional[User]:
        
        if not email or not password:
            return None

        user = await self.user_repository.get_by_email(email.strip().lower())
        if not user:
            return None 
        
        if not self.encrypt_service.verify_password(password, user.password_hash):
            return None 
        
        return user 
        


