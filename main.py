from time import sleep
from system_functions import *
from secrets import password_answer
from password_functions import *


def main_menu():
    clear_screen()
    return_to_menu = True

    print(f"""Options:
new pass   -   create a new password hash in secrets.py
test       -   try to guess the password hashed in secrets.py
exit       -   leave the command-line application""")

    command = input('>').lower()

    if command == 'test':
        password_attempt = input("What's the password?\n")
        access = verify_password(password_attempt, password_answer)

        if access:
            print('Correct!  :D')
        else:
            print('Incorrect...  :(')
    elif command == 'new pass':
        new_pass = input('Give me a new password: ')
        new_hash = create_new_password(new_pass)
        print(new_hash)

        answer = input('Would you like to save this temp pass?\n').lower()
        if answer == 'yes':
            save_new_test_hash(new_hash)
        else:
            pass
    elif command == 'exit':
        return_to_menu = False
    else:
        print(f"'{command}' is not recognised, please try again.")
        sleep(1)
        main_menu()

    if return_to_menu:
        sleep(1)
        main_menu()
    print('Bye-bye!')
    sleep(1)


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("""Why are you trying to exit now?
I added a buit-in feature just for this.

You make me sad.
:(""")
        sleep(3)
        clear_screen()
