from fastapi import APIRouter, Depends 
from typing import List 
from ..dependencies import get_create_product_controller, get_get_all_products_controller, get_get_product_by_id_controller
from ..controllers.create_product_controller import CreateProductRequest, CreateProductResponse, CreateProductController
from ..controllers.get_all_products_controller import GetAllProductsResponse, GetAllProductsController
from ..controllers.get_product_by_id_controller import GetProductByIdRequest, GetProductByIdResponse, GetProductByIdController

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=CreateProductResponse)
async def create_product(request: CreateProductRequest, controller: CreateProductController = Depends(get_create_product_controller)):
    return await controller.handle(request=request)

@router.get("/", response_model=List[GetAllProductsResponse])
async def get_all_products(controller: GetAllProductsController = Depends(get_get_all_products_controller)):
    return await controller.handle()

@router.get("/{product_id}", response_model=GetProductByIdResponse)
async def get_product_by_id(product_id: int, controller: GetProductByIdController = Depends(get_get_product_by_id_controller)):
    request = GetProductByIdRequest(id=product_id)
    return await controller.handle(request=request)