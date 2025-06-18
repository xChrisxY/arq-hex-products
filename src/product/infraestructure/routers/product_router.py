from fastapi import APIRouter, Depends 
from typing import List 
from ..dependencies import get_create_product_controller, get_get_all_products_controller 
from ..controllers.create_product_controller import CreateProductRequest, CreateProductResponse, CreateProductController
from ..controllers.get_all_products_controller import GetAllProductsResponse, GetAllProductsController

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=CreateProductResponse)
async def create_product(request: CreateProductRequest, controller: CreateProductController = Depends(get_create_product_controller)):
    return await controller.handle(request=request)

@router.get("/", response_model=List[GetAllProductsResponse])
async def get_all_products(controller: GetAllProductsResponse = Depends(get_get_all_products_controller)):
    return await controller.handle()