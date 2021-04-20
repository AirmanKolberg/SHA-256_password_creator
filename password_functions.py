import hashlib


def verify_password(user_in_pass, correct_pass_hash):
    user_in_converted = bytes(user_in_pass, 'utf-8')
    user_in_hash = hashlib.sha256(user_in_converted).hexdigest()

    if user_in_hash == correct_pass_hash:
        return True
    else:
        return False


def create_new_password(user_in):
    converted_password = bytes(user_in, 'utf-8')
    password_hash = hashlib.sha256(converted_password).hexdigest()
    return password_hash
