from ...domain.product import Product 
from ...domain.repositories.product_repository import IProductRepository 

class CreateProductUseCase: 
    
    def __init__(self, product_repository: IProductRepository): 
        self.product_repository = product_repository 
        
    async def execute(self, name: str, description: str, price: float) -> Product:
        
        if not name or len(name.strip()) == 0:
            raise ValueError('Product name is required.')

        if price < 0:
            raise ValueError('Product price must be non-negative.')

        product = Product(name=name.strip(), description=description.strip(), price=price)

        return await self.product_repository.create(product=product)