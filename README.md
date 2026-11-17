# Password Hashing & Cracking Lab

## Project Files
* `step1_verify` shows how a simple password can be hashed to turn it into a deterministic fingerprint (the exact same input will always give the exact same output). Also, hashes are one-way and cannot be "decoded" or "reverse engineered". Attackers crack them by guessing inputs until a new hash matches the stolen one.
* `step2_salt` adds another layer to it by "salting" it with `os.urandom(16)` which generates `16 random bytes` when converted with `.hex()`, each byte becomes 2 characters, creating a 32-character hex string.
* `step3_crack` is the "attacker" who managed to stole both the salt and hash then ran through a dictionary attack to crack the salt and hash into the actual password.
* `step4_secure` is a hardened defense using `PBKDF2` (600,000 iterations) with `hmac.compare_digest` to stop brute force speed and timing attacks since it always takes the exact same amount of time to compare two strings meanwhile, `==` stops checking the exact microsecond it sees one wrong letter, letting advanced attackers measure response times to guess hashes.

## Key Security Takeaways
* `Salts` are random bytes turn into hex(16) that is human readable but makes no actual sense.
* Plain `SHA-256` is too fast to be cracked because a rainbow table can be used to crack it.
* `PBKDF2` + `hmac.compare_digest` solves this problem because the `600,000 iterations` is what creates the 0.2-second delay for one login. The 0.2-second delay gets multiplied by the number of guesses in the attacker's wordlist (example: 1,000,000 guesses * 0.2 seconds = days/months)