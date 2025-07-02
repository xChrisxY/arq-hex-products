from fastapi import HTTPException, status 
from pydantic import BaseModel 
from datetime import datetime

from ...application.uses_cases.get_product_by_id_use_case import GetProductsByIdUseCase

class GetProductByIdRequest(BaseModel):
    id: int
    
class GetProductByIdResponse(BaseModel):
    id: int 
    name: str 
    description: str 
    price: float 
    created_at: datetime
    updated_at: datetime

class GetProductByIdController:
    
    def __init__(self, get_product_by_id_use_case: GetProductsByIdUseCase):
        self.get_product_by_id_use_case = get_product_by_id_use_case 
        
    async def handle(self, request: GetProductByIdRequest) -> GetProductByIdResponse:
        try:
            product = await self.get_product_by_id_use_case.execute(request.id)
            
            return GetProductByIdResponse(
                id=product.id,
                name=product.name,
                description=product.description,
                price=product.price,
                created_at=product.created_at,
                updated_at=product.updated_at            
            )
            
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
    
    