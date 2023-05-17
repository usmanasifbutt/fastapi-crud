from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Password():
    def encrypt(password: str):
        return pwd_cxt.hash(password)
    
    def decrypt(password, plain_password):
        return pwd_cxt.verify(plain_password, password)