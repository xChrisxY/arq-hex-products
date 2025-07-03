from ..domain.repositories.product_repository import IProductRepository
from ..domain.product import Product

from database.mysql import get_db_session
from database.entities.product_entity import ProductEntity

from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from typing import List

class MySQLProductRepository(IProductRepository):
    
    def __init__(self):
        
        self.get_db = get_db_session # get_db_session ahora es una función asíncrona generadora, le pasamos como referencia

    async def create(self, product: Product) -> Product:
        # Usamos 'async with' para gestionar la sesión de forma asíncrona
        async with self.get_db() as db_session: 

            try:
                
                product_entity = ProductEntity(
                    name=product.name,
                    description=product.description,
                    price=product.price
                )
                
                db_session.add(product_entity)
                await db_session.commit()
                # Esto refresca el objeto con el ID generado, etc.
                await db_session.refresh(product_entity)

                # Convertir de entidad a modelo de dominio
                domain_product = Product(
                    id=product_entity.id, 
                    name=product_entity.name, 
                    description=product_entity.description, 
                    price=product_entity.price,
                    created_at=product_entity.created_at, 
                    updated_at=product_entity.updated_at
                )

                return domain_product
            
            except IntegrityError as e: 
                await db_session.rollback()
                # Podemos lanzar una excepción de dominio aquí si es relevante 
                raise ValueError(f"Error de integridad al crear el producto: {e}")
            
            except Exception as error: 
                await db_session.rollback()
                print(f"Error al crear el producto: {error}")
                raise error # Re-lanzar el error la excepción para que maneje la capa superior

    
    async def get_all(self) -> List[Product]:
        async with self.get_db() as db_session:
            
            try: 
                
                statement = select(ProductEntity)
                results = await db_session.exec(statement)
                product_entities = results.all()
                
                if not product_entities:
                    return [] 
                
                products = [
                    Product(
                        id=domain_product.id, 
                        name=domain_product.name, 
                        description=domain_product.description, 
                        price=domain_product.price,
                        created_at=domain_product.created_at, 
                        updated_at=domain_product.updated_at
                    ) 
                    for domain_product in product_entities
                ]

                return products
            
            except Exception as error:
                print(f"Error al obtener los productos: {error}")
                return []
            
    async def get_by_id(self, product_id):
        async with self.get_db() as db_session: 
            
            try: 
            
                statement = select(ProductEntity).where(ProductEntity.id == product_id)
                results = await db_session.exec(statement)
                product_entity = results.first()
                
                if not product_entity:
                    return None 
                
                domain_product = Product(
                    id=product_entity.id, 
                    name=product_entity.name, 
                    description=product_entity.description, 
                    price=product_entity.price,
                    created_at=product_entity.created_at, 
                    updated_at=product_entity.updated_at
                ) 
                
                return domain_product
            
            except Exception as error:
                print(f"Error al obtener producto por ID: {error}")
                return None