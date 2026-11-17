import hashlib
import time

stolen_salt = "dcd1b919135744b1769f6fc57095ce0b"
stolen_hash = "4eed0d1b8bec6abd2d86d164626386a21b16c2113412631f12a2844f3e99b757"

wordlist = ["123456", "password", "imissyou", "GodisGood", "iloveyouchynna", "allenpogi123"]

start_time = time.time()

for guess in wordlist: 
    guess_attempt = stolen_salt + guess
    guess_hash = hashlib.sha256(guess_attempt.encode('utf-8')).hexdigest()
    if guess_hash == stolen_hash:
        elapsed_time = time.time() - start_time
        print(f"WASAK! Password is: {guess} | Time: {elapsed_time}")
        break