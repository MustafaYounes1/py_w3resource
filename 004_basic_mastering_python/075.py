"""

Generate a random password of a length 10 that combines upper case and lower case characters with some digits.

"""

import random
import string


def main():
    random.seed(0)
    allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits
    print(
        "".join([random.choice(allowed) for _ in range(10)])
    )


if __name__ == "__main__":
    main()
