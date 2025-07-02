import re 
from ...domain.user import User 
from ...domain.user_repository import IUserRepository 
from ..services.encrypt_service import IEncryptService

class CreateUserUseCase:
    
    def __init__(self, user_repository: IUserRepository, encrypt_service: IEncryptService): 
        self.user_repository = user_repository 
        self.encrypt_service = encrypt_service
        
    async def execute(self, username: str, email: str, password: str) -> User: 
        
        if not self._is_valid_email(email):
            raise ValueError('Invalid email format')
        
        existing_user_email = self.user_repository.get_by_email(email) 
        if existing_user_email:
            raise ValueError('User with this email already exists')
        
        existing_user_username = self.user_repository.get_by_username(username)
        if existing_user_username: 
            raise ValueError('User with this username already exists')

        # Crear el usuario 
        password_hash = self.encrypt_service.hash_password(password)
        
        user = User(
            username=username.strip(), 
            email=email.strip().lower(),
            password_hash=password_hash
        )
        
        return await self.user_repository.create(user)
    
    def _is_valid_email(self, email: str) -> bool: 
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.match(pattern, email) is not None