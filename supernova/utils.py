import hashlib
def md5_encoding(public_string: str) -> str:
    m = hashlib.md5()
    m.update(public_string.encode("utf8"))
    return m.hexdigest()