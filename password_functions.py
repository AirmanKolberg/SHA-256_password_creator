import hashlib


def verify_password(user_pass, correct_password):
    user_pass_converted = bytes(user_pass, 'utf-8')
    password_guess = hashlib.sha256(user_pass_converted).hexdigest()

    if password_guess == correct_password:
        return True
    else:
        return False


def create_new_password(user_in):
    converted_password = bytes(user_in, 'utf-8')
    password_hash = hashlib.sha256(converted_password).hexdigest()
    return password_hash
