from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def get_key(user_key: str) -> bytes:
    return hashlib.md5(user_key.encode()).digest()  # AES-128 = 16 byte key

def encrypt_file(data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data, AES.block_size))

def decrypt_file(data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(data), AES.block_size)
