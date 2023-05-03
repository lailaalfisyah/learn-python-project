import random
import string

def random_string(length:int) -> str:
    data = ''.join(random.choice(string.ascii_letters) for i in range(6))
    return data