import os
import hashlib

password = "iloveyouchynna"

salt = os.urandom(16).hex()
salted = salt + password
saved_hash = hashlib.sha256(salted.encode('utf-8')).hexdigest()

print(salt)
print(saved_hash)

login_attempt = input("Enter Password: ")

attempt_hash = salt + login_attempt
saved_attempt = hashlib.sha256(attempt_hash.encode('utf-8')).hexdigest()

if saved_attempt == saved_hash:
    print("Login successful!")
else:
    print("Wrong Password!")