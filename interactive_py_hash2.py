# %%
import hashlib

print(hashlib.algorithms_available)

# %%
text = "This a secret text, don't read it!"
encoded = hashlib.sha256(text.encode())
print(encoded.hexdigest())

# %%
for alg in hashlib.algorithms_guaranteed:
    res = getattr(hashlib, alg)(text.encode())
    try:
        print(alg, res.hexdigest())
    except:
        print(alg, '???')

# %%
