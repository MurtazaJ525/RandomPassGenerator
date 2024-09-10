import random
import string


# EASY LEVEL - Order not randomised
def generate_easy_password(nr_letters, nr_symbols, nr_numbers):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password = ''
    password += ''.join(random.choice(letters) for _ in range(nr_letters))
    password += ''.join(random.choice(symbols) for _ in range(nr_symbols))
    password += ''.join(random.choice(numbers) for _ in range(nr_numbers))

    return password


# HARD LEVEL - Order of characters randomised
def generate_hard_password(nr_letters, nr_symbols, nr_numbers):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    return ''.join(password_list)


def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    # Generate passwords
    easy_password = generate_easy_password(nr_letters, nr_symbols, nr_numbers)
    hard_password = generate_hard_password(nr_letters, nr_symbols, nr_numbers)

    # Print results
    print(f"Your easy-level password is: {easy_password}")
    print(f"Your hard-level password is: {hard_password}")


if __name__ == "__main__":
    main()
