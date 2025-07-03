from ..application.uses_cases.create_user_use_case import CreateUserUseCase
from ..application.uses_cases.auth_user_use_case import AuthServiceUseCase
from .mysql_user_repository import MySQLUserRepository
from .services.encrypt_service import SimpleEncryptService
from .controllers.create_user_controller import CreateUserController
from .controllers.auth_user_controller import AuthUserController

_user_repository = MySQLUserRepository()
_encrypt_service = SimpleEncryptService()
_create_user_use_case = CreateUserUseCase(_user_repository, _encrypt_service)
_auth_user_use_case = AuthServiceUseCase(_user_repository, _encrypt_service)

def get_create_user_controller() -> CreateUserController:
    return CreateUserController(_create_user_use_case)

def get_auth_user_controller() -> AuthUserController:
    return AuthUserController(_auth_user_use_case)