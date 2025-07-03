from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import datetime, timezone

class UserEntity(SQLModel, table=True):
    
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    username: str = Field(unique=True, index=True, max_length=100)
    email: str = Field(unique=True, index=True, max_length=255)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": datetime.now(timezone.utc)})
    
    