from abc import ABC, abstractmethod 
from typing import List, Optional 
from ..product import Product 

class IProductRepository(ABC):
    
    @abstractmethod 
    async def create(self, product: Product) -> Product: 
        pass 
    
    @abstractmethod 
    async def get_all(self) -> List[Product]:
        pass 
    
    @abstractmethod 
    async def get_by_id(self, product_id: int) -> Optional[Product]: 
        pass 
    
    