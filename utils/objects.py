import string
import random


class Utilities:
    @staticmethod
    def random_string(length):
        return ''.join(random.choice(string.ascii_letters) for m in range(length))


