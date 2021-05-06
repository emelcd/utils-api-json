from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat, BestAvailableEncryption

from uuid import uuid4 as ui

class Client:
    def __init__(self, passw):
        self.ui = ui()
        self.passw = passw
        self.key = self.gen_key()
        self.priS = self.pri_key_s()
        self.pubS = self.pub_key_s()
        # self.save()
    def gen_key(self):
        ky_size = 4096
        pri = rsa.generate_private_key(65537, key_size=ky_size)
        return pri
    def pri_key_s(self):
        passw = self.passw.encode('utf-8')
        pri_k = self.key.private_bytes(
            encoding=Encoding.PEM, 
            format=PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=BestAvailableEncryption(passw)
        )
        return pri_k
    def pub_key_s(self):
        pub_k = self.key.public_key().public_bytes(
            encoding=Encoding.PEM,
            format=PublicFormat.SubjectPublicKeyInfo
        )
        return pub_k
    def save(self):
        with open('key.pem','w') as f:
            f.write(self.priS.decode('utf-8'))   







