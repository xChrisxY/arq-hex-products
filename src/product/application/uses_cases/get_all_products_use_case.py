from ...domain.product import Product 
from ...domain.repositories.product_repository import IProductRepository 

from typing import List

class GetAllProductsUseCase: 
    
    def __init__(self, product_repository: IProductRepository): 
        self.product_repository = product_repository 
        
    async def execute(self) -> List[Product]:
        return await self.product_repository.get_all()