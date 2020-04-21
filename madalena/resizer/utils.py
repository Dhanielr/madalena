import random
import string

def random_chars(y):
    return ''.join(random.choice(string.hexdigits) for x in range(y)) 
