from fastapi import HTTPException, status 
from pydantic import BaseModel 
from typing import List
from application.uses_cases.get_all_products_use_case import GetAllProductsUseCase 

class GetAllProductsResponse(BaseModel): 
    id: int
    name: str
    description: str 
    price: float 
    created_at: str 
    updated_at: str 


class GetAllProductsController:

    def __init__(self, get_all_products_use_case: GetAllProductsUseCase):
        self.get_all_products_use_case = get_all_products_use_case 
        
    async def handle(self) -> List[GetAllProductsResponse]:
        
        try: 
            
            products = await self.get_all_products_use_case.execute()

            products_response = [

                GetAllProductsResponse(
                    id=product.id, 
                    name=product.name, 
                    description=product.description, 
                    price=product.price, 
                    created_at=product.created_at.iso_format(), 
                    updated_at=product.updated_at.iso_format()
                ) 

                for product in products
            ]
            
            return products_response
            
        except Exception as e:
            return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))    
        
        