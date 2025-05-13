from cryptography.fernet import Fernet
import hashlib

# Generar clave y cifrar mensaje
clave = Fernet.generate_key()
cifrador = Fernet(clave)

mensaje = "Este es un mensaje secreto".encode()
cifrado = cifrador.encrypt(mensaje)
descifrado = cifrador.decrypt(cifrado)

print("Mensaje original:", mensaje.decode())
print("Cifrado:", cifrado)
print("Descifrado:", descifrado.decode())

# Hash de contraseña
contraseña = "mi_secreta"
hash = hashlib.sha256(contraseña.encode()).hexdigest()
print("Hash SHA-256:", hash)