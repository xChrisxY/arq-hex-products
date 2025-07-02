from abc import ABC, abstractmethod

class IEncryptService(ABC): 
    @abstractmethod
    def hash_password(self, password: str) -> str: 
        pass 
    
    @abstractmethod 
    def verify_password(self, password: str, hashed_password: str) -> bool: 
        pass 
    
    