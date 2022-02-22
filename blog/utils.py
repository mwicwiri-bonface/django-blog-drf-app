from random import randint


def generate_key(min_length=20, max_length=20, use_lower=True, use_upper=True, use_numbers=True, use_special=False):
    charset = ''
    if use_lower:
        charset += "abcdefghijklmnopqrstuvwxyz"
    if use_upper:
        charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_numbers:
        charset += "123456789"
    if use_special:
        charset += "~@#$%^*()_+-={}|]["
    if min_length > max_length:
        length = randint(max_length, min_length)
    else:
        length = randint(min_length, max_length)
    key = ''
    for i in range(0, length):
        key += charset[(randint(0, len(charset) - 1))]
    return key
