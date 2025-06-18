from application.uses_cases.create_product_use_case import CreateProductUseCase 
from application.uses_cases.get_all_products_use_case import GetAllProductsUseCase

from .controllers.create_product_controller import CreateProductController
from .controllers.get_all_products_controller import GetAllProductsController 

from .in_memory_product_repository import InMemoryProductRepository

_productRepository = InMemoryProductRepository()

_createProductUseCase = CreateProductUseCase(_productRepository)
_getAllProductsUseCase = GetAllProductsUseCase(_productRepository)

def get_create_product_controller() -> CreateProductController:
    return CreateProductController(_createProductUseCase)

def get_get_all_products_controller() -> GetAllProductsController:
    return GetAllProductsController(_getAllProductsUseCase)



