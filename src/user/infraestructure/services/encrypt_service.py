import hashlib 
import secrets 
from ...application.services.encrypt_service import IEncryptService 

class SimpleEncryptService(IEncryptService): 
    
    """
    Implementación simple de encriptación usando hashlib.
    En producción usaremos bycript
    """
    
    def hash_password(self, password: str) -> str:
        
        salt = secrets.token_hex(16)
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), salt.encode(), 100000)
        
        return f"{salt}:{password_hash.hex()}"

    def verify_password(self, password: str, hashed_password: str) -> bool:

        try: 
            
            salt, stored_hash = hashed_password.split(':')
            password_hash = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), salt.encode(), 100000)
            return password_hash.hex() == stored_hash
            
        except ValueError:
            return False
        