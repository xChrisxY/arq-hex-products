from ..application.uses_cases.create_user_use_case import CreateUserUseCase
from .mysql_user_repository import MySQLUserRepository
from .services.encrypt_service import SimpleEncryptService
from .controllers.create_user_controller import CreateUserController

_user_repository = MySQLUserRepository()
_encrypt_service = SimpleEncryptService()
_create_user_use_case = CreateUserUseCase(_user_repository, _encrypt_service)

def get_create_user_controller() -> CreateUserController:
    return CreateUserController(_create_user_use_case)
