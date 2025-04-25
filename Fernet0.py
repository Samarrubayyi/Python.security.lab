from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)


message = b"My encrypted message"

 
encrypted_message = cipher.encrypt(message)
print("Encrypted:", encrypted_message)


decrypted_message = cipher.decrypt(encrypted_message)
print("Decrypted:", decrypted_message.decode())