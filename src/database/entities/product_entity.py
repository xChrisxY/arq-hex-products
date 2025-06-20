from sqlmodel import SQLModel, Field, Relationship 
from typing import Optional, List
from datetime import datetime, timezone

class ProductEntity(SQLModel, table=True): 

    __tablename__ = "products"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(index=True, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    price: float = Field(ge=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": datetime.now(timezone.utc)})