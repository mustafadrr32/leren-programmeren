import random
import string

for x in range(50):
    def generate_password():
        while True:
            num_uppercase = random.randint(2, 6)
            uppercase_letters = random.sample(string.ascii_uppercase, num_uppercase)

            lowercase_letters = random.choices(string.ascii_lowercase, k=8)

            special_characters = random.sample("@#$%&?_", 3)

            num_digits = 7 - num_uppercase
            digits = random.choices(string.digits, k=num_digits)

            password = uppercase_letters + lowercase_letters + special_characters + digits
            random.shuffle(password)

            password_str = ''.join(password)

            if (password_str[1].isupper() or password_str[-1].islower() or password_str[0] in string.digits or password_str[:3].isdigit() or password_str[-1] in string.punctuation):
                continue
            else:
                return password_str

    print(generate_password())