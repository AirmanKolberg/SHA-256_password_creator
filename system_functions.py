from os import system


def bash_command(user_in):
    _ = system(user_in)


def clear_screen():
    bash_command('clear')


def save_new_test_hash(new_hash):
    bash_command(f"""rm secrets.py && echo "password_answer = '{new_hash}'" >> secrets.py""")
