import hashlib

password = "iloveyouchynna"
saved_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
print(saved_hash)

login_attempt = input("Enter Password: ")
attempt_hash = hashlib.sha256(login_attempt.encode('utf-8')).hexdigest()
if attempt_hash == saved_hash:
    print("Login successful!")
else:
    print("Wrong Password!")
