from dataclasses import dataclasss
from typing import Optional 
from datetime import datetime 

@dataclasss
class Product: 
    id: Optional[int] = None 
    name: str = ""
    description: str = ""
    price: float = 0.0 
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None 
    
    
    