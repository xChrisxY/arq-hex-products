from ...domain.product import Product
from ...domain.repositories.product_repository import IProductRepository
from typing import Optional

class GetProductsByIdUseCase:
    
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository 
        
    async def execute(self, product_id: int) -> Optional[Product]:
        print("aquii")
        return await self.product_repository.get_by_id(product_id=product_id)