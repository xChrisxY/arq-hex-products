from fastapi import HTTPException, status
from pydantic import BaseModel
from datetime import datetime

from ...application.uses_cases.create_user_use_case import CreateUserUseCase

class CreateUserRequest(BaseModel): 
    
    username: str 
    email: str 
    password_hash = str 

class CreateUserResponse(BaseModel):

    id: int
    username: str 
    email: str 
    created_at: datetime
    updated_at: datetime

class CreateUserController:
    
    def __init__(self, create_user_use_case: CreateUserUseCase):
        self.create_user_use_case = create_user_use_case

    async def handle(self, request: CreateUserRequest) -> CreateUserResponse:
        
        try: 
        
            user = await self.create_user_use_case.execute(
                username=request.username, 
                email=request.email, 
                password=request.password_hash
            )
            
            return CreateUserResponse(
                id=user.id, 
                username=user.username, 
                email=user.email, 
                created_at=user.created_at.isoformat(), 
                updated_at=user.updated_at.isoformat(),
            )
        
        
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))