import random
import string

MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 30
DEFAULT_PASSWORD_LENGTH = 16
DEFAULT_AMOUNT_PASSWORDS = 1
DEFAULT_PASSWORD_SYMBOLS = "both"
DEFAULT_AMOUNT_USERNAMES = 1
DEFAULT_AMOUNT_WORDS = 2
DEFAULT_AMOUNT_INTEGERS = 2
DEFAULT_STARTING_WORD = "no"
starting_word = ""

CHARACTERS = string.ascii_lowercase + string.ascii_uppercase
NUMBERS = string.digits


def get_password_length(default):
    while True:
        password_len = input(f"Choose password length between {MIN_PASSWORD_LENGTH} "
                             f"and {MAX_PASSWORD_LENGTH} (Default={DEFAULT_PASSWORD_LENGTH}): ")

        if password_len == "":
            return default
        try:
            int_pass_length = int(password_len)
            if not 6 <= int_pass_length <= 30:
                print(f"Please enter a valid length.")
            else:
                break
        except ValueError:
            print(f"Please enter a valid length.")
    return int(password_len)


def get_password_symbols(chars, nums, default):
    password_symbols = ""
    char_word_list = ["chars", "characters", "char", "c"]
    num_word_list = ["numbers", "nums", "num", "n", "number"]
    both_word_list = ["both", "b", "all", ""]
    allowed_answers = char_word_list + num_word_list + both_word_list
    while True:
        user_password_selection = input(
            f"Select characters (p) or numbers (n), or both (b) (Default={default}): ").lower()
        if user_password_selection not in allowed_answers:
            print(f"Enter a valid answer.")
            continue
        if user_password_selection in both_word_list:
            password_symbols += chars + nums
        elif user_password_selection in char_word_list:
            password_symbols += chars
        elif user_password_selection in num_word_list:
            password_symbols += nums

        break
    return password_symbols


def get_random_password(pass_length, symbols):
    random_password = ""
    for i in range(pass_length):
        random_password += random.choice(symbols)
    return random_password


def get_amount_passwords(default):
    while True:
        amount_passwords = input(f"How many passwords would you like to generate (Default={default}): ")
        if amount_passwords.isdigit():
            int_amount = int(amount_passwords)
            return int_amount
        elif amount_passwords == "":
            return default
        else:
            print(f"Please enter a valid integer")


def main_func_passwords():
    amount_passwords = get_amount_passwords(DEFAULT_AMOUNT_PASSWORDS)
    pass_length = get_password_length(DEFAULT_PASSWORD_LENGTH)
    all_symbols = get_password_symbols(CHARACTERS, NUMBERS, DEFAULT_PASSWORD_SYMBOLS)
    for i in range(amount_passwords):
        print(f"-" * 30)
        random_password = get_random_password(pass_length, all_symbols)
        print(random_password)


WORDS = ["dynamite", "tron", "wannabe", "yasuo", "apple", "strict", "daddy", "egirl", "broken", "fame", "arrogant",
             "lighter", "resist", "window", "moon", "glider", "femboy"]


def get_starting_word():
    while True:
        user_input = input(f"Would you like your usernames to start with word"
                           f" (type the word | no) (default={DEFAULT_STARTING_WORD}): ")

        if len(user_input) < 3 and user_input != "":
            print(f"Your word must have at least 3 characters.")
            continue

        return user_input


def get_amount_usernames(default):
    while True:
        amount_usernames = input(f"How many usernames would you like to generate (Default={default}): ")
        if amount_usernames.isdigit():
            int_amount = int(amount_usernames)
            return int_amount
        elif amount_usernames == "":
            return default
        else:
            print(f"Please enter a valid integer")


def get_amount_words(default):
    while True:
        amount_words = input(f"Choose how many random words should be selected (Default={DEFAULT_AMOUNT_WORDS}): ")
        if amount_words.isdigit() and int(amount_words) > 0:
            int_amount = int(amount_words)
            return int_amount
        elif amount_words == "":
            return default
        elif int(amount_words) == 0:
            print("You must have at least 1 word.")
        else:
            print(f"Please enter a valid integer")


def get_amount_integers(default):
    while True:
        amount_integers = input(
            f"Choose how many random integers should be selected (Default={DEFAULT_AMOUNT_INTEGERS}): ")
        if amount_integers.isdigit():
            int_amount = int(amount_integers)
            return int_amount
        elif amount_integers == "":
            return default
        else:
            print(f"Please enter a valid integer")


def get_username_format():
    username_starting_word = get_starting_word()
    amount_words = get_amount_words(DEFAULT_AMOUNT_WORDS)
    amount_integers = get_amount_integers(DEFAULT_AMOUNT_INTEGERS)
    if username_starting_word:
        print(f"You've selected starting word '{username_starting_word}' with "
              f"{amount_words} random words and {amount_integers} integers at the end format.")
    else:
        print(f"You've selected {amount_words} random words with {amount_integers} integers at the end format.")
    return amount_words, amount_integers, username_starting_word


def get_username(amount_words, amount_integers, user_starting_word):
    random_username = f"{user_starting_word}"

    for i in range(amount_words):
        random_username += random.choice(WORDS)

    for i in range(amount_integers):
        random_username += random.choice(NUMBERS)

    return random_username


def main_func_username():
    amount_usernames = get_amount_usernames(DEFAULT_AMOUNT_USERNAMES)
    username_words, username_integers, user_starting_word = get_username_format()
    print(f"You've generated {amount_usernames} usernames:")
    for i in range(amount_usernames):
        print("-" * 30)
        print(get_username(username_words, username_integers, user_starting_word))


def main_function_selection():
    username_words = ["u", "username", "name", "usernames", "users"]
    password_words = ["p", "password", "pass", "passwords"]
    while True:
        user_answer = input("What would you like to generate? ('u' for username | 'p' for password): ").lower()

        if user_answer in username_words:
            main_func_username()
            break
        elif user_answer in password_words:
            main_func_passwords()
            break
        else:
            print(f"Please enter a valid answer.")


if __name__ == "__main__":
    main_function_selection()
