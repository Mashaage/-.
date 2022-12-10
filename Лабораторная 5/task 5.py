import random

def get_random_password() -> str:

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    m = alphabet + alphabet_ + digits
    return random.sample(m, 8)

print(get_random_password())