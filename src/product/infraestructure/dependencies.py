from ..application.uses_cases.create_product_use_case import CreateProductUseCase 
from ..application.uses_cases.get_all_products_use_case import GetAllProductsUseCase
from ..application.uses_cases.get_product_by_id_use_case import GetProductsByIdUseCase

from .controllers.create_product_controller import CreateProductController
from .controllers.get_all_products_controller import GetAllProductsController 
from .controllers.get_product_by_id_controller import GetProductByIdController

from .mysql_product_repository import MySQLProductRepository

_productRepository = MySQLProductRepository()

_createProductUseCase = CreateProductUseCase(_productRepository)
_getAllProductsUseCase = GetAllProductsUseCase(_productRepository)
_getProductByIdUseCase = GetProductsByIdUseCase(_productRepository)

def get_create_product_controller() -> CreateProductController:
    return CreateProductController(_createProductUseCase)

def get_get_all_products_controller() -> GetAllProductsController:
    return GetAllProductsController(_getAllProductsUseCase)

def get_get_product_by_id_controller() -> GetProductByIdController:
    return GetProductByIdController(_getProductByIdUseCase)



