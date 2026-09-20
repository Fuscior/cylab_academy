import hashlib

h = hashlib.sha256(b"BENNETT").hexdigest()
key = ''.join(h[i] for i in [4, 5, 3, 6, 2, 7, 1, 8])


print(key)