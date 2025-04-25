import rsa


public_key, private_key = rsa.newkeys(512)


message = "My secret message"


enc_message = rsa.encrypt(message.encode(), public_key)


dec_message = rsa.decrypt(enc_message, private_key).decode()


print("\nOriginal message:", message)
print("Encrypted message:", enc_message)
print("Decrypted message:", dec_message)