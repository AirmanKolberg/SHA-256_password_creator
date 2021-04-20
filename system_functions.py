from os import system


def clear_screen():
    _ = system('clear')


def bash_input(user_in):
    _ = system(user_in)


def save_new_test_hash(new_hash):
    bash_input(f"""rm secrets.py && echo "password_answer = '{new_hash}'" >> secrets.py""")
