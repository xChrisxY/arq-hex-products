from fastapi import HTTPException, status 
from pydantic import BaseModel 
from ...application.uses_cases.auth_user_use_case import AuthServiceUseCase 

class AuthUserRequest(BaseModel):
    email: str 
    password: str 
    
class AuthUserResponse(BaseModel):
    id: int 
    username: str 
    email: str 
    message: str 
    
class AuthUserController:
    
    def __init__(self, auth_user_use_case: AuthServiceUseCase):
        self.auth_user_use_case = auth_user_use_case 
        
    async def handle(self, request: AuthUserRequest) -> AuthUserResponse:
        
        try:
            
            user = await self.auth_user_use_case.execute(
                email=request.email, 
                password=request.password
            )

            if not user:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password.")
            
            return AuthUserResponse(
                id=user.id, 
                username=user.username, 
                email=user.email,
                message="Authentication succesfull"
            )
        
        except HTTPException:
            raise
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))