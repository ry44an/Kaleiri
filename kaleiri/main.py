import string
import hashlib

def hash_text(text, algorithm):
    algorithm = algorithm.lower()
    """Hashes the given text using the specified algorithm."""
    if algorithm == 'md5':
        hash_object = hashlib.md5()
    elif algorithm == 'sha-1':
        hash_object = hashlib.sha1()
    elif algorithm == 'sha-224':
        hash_object = hashlib.sha224()
    elif algorithm == 'sha-256':
        hash_object = hashlib.sha256()
    elif algorithm == 'sha-384':
        hash_object = hashlib.sha384()
    elif algorithm == 'sha-512':
        hash_object = hashlib.sha512()
    elif algorithm == 'sha3-224':
        hash_object = hashlib.sha3_224()
    elif algorithm == 'sha3-256':
        hash_object = hashlib.sha3_256()
    elif algorithm == 'sha3-384':
        hash_object = hashlib.sha3_384()
    elif algorithm == 'sha3-512':
        hash_object = hashlib.sha3_512()
    else:
        raise ValueError("Invalid hash algorithm specified.")
        
    hash_object.update(text.encode())
    return hash_object.hexdigest()

def iterate_characters(hash, algorithm):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        for length in range(1, len(characters) + 1):
            for combo in generate_combinations(characters.lower(), length):
                combohashed = hash_text(combo, algorithm)
                if combohashed == hash:
                    return combo
                else:
                    pass

def generate_combinations(characters, length):
    if length == 1:
        return list(characters)
    else:
        return [a + b for a in characters for b in generate_combinations(characters, length - 1)]