def encode_password(password: str) -> str:
    return ''.join(reversed(list(password)))

def decode_password(password: str) -> str:
    return ''.join(reversed(list(password)))