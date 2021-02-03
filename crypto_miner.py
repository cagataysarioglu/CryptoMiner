from hashlib import sha256
MAX_NONCE = 100000000000

def cryptographicalSha256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = cryptographicalSha256(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined crypto coins with nonce value: {nonce}")
            return new_hash
    raise BaseException(f"Could not find correct hash after trying {MAX_NONCE} times.")

if __name__ == "__main__":
    transactions = "Cagatay -> Kursad, Bumin -> Sencer"
    difficulty = 7 # The larger the number, the longer the working time.
    import time
    start = time.time()
    print("Start mining")
    new_hash = mine(5, transactions, "0000000xc079338a713644egd56032csh3z55233r19s82145fmk34u639", difficulty)
    total_time = str((time.time() - start))
    print(f"End mining. Mining took {total_time} seconds.")
    print(new_hash)
