from fastapi import HTTPException, status 
from pydantic import BaseModel 
from typing import List
from ...application.uses_cases.get_all_products_use_case import GetAllProductsUseCase 

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
            print(f"Los productos son: {products}")

            products_response = [

                GetAllProductsResponse(
                    id=product.id, 
                    name=product.name, 
                    description=product.description, 
                    price=product.price, 
                    created_at=product.created_at.isoformat() if product.created_at else None, 
                    updated_at=product.updated_at.isoformat() if product.updated_at else None,
                ) 

                for product in products
            ]
            return products_response
            
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))    
        
        