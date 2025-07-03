from fastapi import APIRouter, Depends 
from ..dependencies import get_create_user_controller, get_auth_user_controller
from ..controllers.create_user_controller import CreateUserController, CreateUserRequest, CreateUserResponse
from ..controllers.auth_user_controller import AuthUserController, AuthUserRequest, AuthUserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=CreateUserResponse)
async def register_user(request: CreateUserRequest, controller: CreateUserController = Depends(get_create_user_controller)):
    return await controller.handle(request)

@router.post("/login", response_model=AuthUserResponse)
async def login_user(request: AuthUserRequest, controller: AuthUserController = Depends(get_auth_user_controller)):
    return await controller.handle(request)