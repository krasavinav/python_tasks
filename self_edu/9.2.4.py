from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase

import random

random.seed(1)
indx = random.randint(0, len(chars) - 1)
