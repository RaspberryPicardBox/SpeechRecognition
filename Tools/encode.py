import hashlib

def encode(text):
    encoded = hashlib.sha384(text.encode('utf-8')).hexdigest()
    return encoded

print(encode("text"))
