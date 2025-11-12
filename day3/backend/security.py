from argon2 import PasswordHasher

ph = PasswordHasher()


def hash_password(password):
    if not password:
        return None, False
    return ph.hash(password), True

def verify_password(stored_password, provided_password):
    try:
        return ph.verify(stored_password, provided_password)
    except:
        return False