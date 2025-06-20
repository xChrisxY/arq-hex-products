from typing import List, Optional 
from datetime import datetime 
from domain.product import Product 
from product.domain.repositories.product_repository import IProductRepository 

class InMemoryProductRepository(IProductRepository):
    
    def __init__(self):
        self._products: List[Product] = []
        self._next_id: int = 1 
        
    async def create(self, product: Product) -> Product: 
        now = datetime.now()
        product.id = self._next_id 
        product.created_at = now 
        product.updated_at = now 
        
        self._products.append(product)
        self._next_id += 1 
        
        return product 
    
    async def get_all(self) -> List[Product]:
        return self._products.copy()
    
    async def get_by_id(self, product_id) -> Optional[Product]:
        for product in self._products: 
            if product.id == product_id:
                return product 
            
        return None

    
