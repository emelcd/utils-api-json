from cryptography.fernet import Fernet
from uuid import uuid4

class User:
    def __init__(self):
        self.fk = Fernet.generate_key()
        self.obj=Fernet(self.fk)
    def encrypt_sys(self, string):
        return self.obj.encrypt(string.encode('utf-8'))
    def give_obj(self):
        return self.fk

print(User().encrypt_sys("0"))