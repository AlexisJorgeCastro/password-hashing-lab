import hashlib
import os
import hmac

password = "iloveyouchynna"

salt = os.urandom(16) # No .hex() because pbkdf2_hmac expects raw bytes for the salt

saved_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 600000).hex()
print(saved_hash)

login_attempt = input("Enter Password: ")
attempt_hash = hashlib.pbkdf2_hmac('sha256', login_attempt.encode('utf-8'), salt, 600000).hex()
print(attempt_hash)

if hmac.compare_digest(attempt_hash, saved_hash):
    print("Login Successful!")
else:
    print("Wrong Password")