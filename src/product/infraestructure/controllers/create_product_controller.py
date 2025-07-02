from fastapi import HTTPException, status
from pydantic import BaseModel 
from datetime import datetime

from ...application.uses_cases.create_product_use_case import CreateProductUseCase 

class CreateProductRequest(BaseModel): 
    
    name: str 
    description: str 
    price: float 
    
class CreateProductResponse(BaseModel): 
    
    id: int 
    name: str 
    description: str 
    price: float 
    created_at: str 
    updated_at: str 
    
class CreateProductController: 
    
    def __init__(self, create_product_use_case: CreateProductUseCase):
        self.create_product_use_case = create_product_use_case
        
    async def handle(self, request: CreateProductRequest) -> CreateProductRequest: 
        try:
            product = await self.create_product_use_case.execute(
                name=request.name, 
                description=request.description, 
                price=request.price, 
            )

            return CreateProductResponse(
                id=product.id, 
                name=product.name, 
                description=product.description, 
                price=product.price,
                created_at=product.created_at.isoformat(), 
                updated_at=product.updated_at.isoformat(),
            )
            
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e: 
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
        