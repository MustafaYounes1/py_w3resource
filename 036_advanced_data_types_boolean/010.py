"""

Write a Python program that checks a simple authentication system. The program verifies the provided username and
password against predefined usernames and passwords by using boolean checks.

predefined_users = {
    "empdb1": "Jue@3$juy0",
    "empdb2": "juRe34@$",
    "admin": "koiUaq$&@ki"
}

users = ["empdb1", "admin", "sd"]
passwords = ["Jue@3$juy0", "oiUaq$&@ki", "sds"]

=> True, False, False

"""


def main():
    predefined_users = {
        "empdb1": "Jue@3$juy0",
        "empdb2": "juRe34@$",
        "admin": "koiUaq$&@ki"
    }

    users = ["empdb1", "admin", "sd"]
    passwords = ["Jue@3$juy0", "oiUaq$&@ki", "sds"]

    for u, ps in zip(users, passwords):
        if u in predefined_users:
            print(predefined_users[u] == ps)
        else:
            print(False)


if __name__ == "__main__":
    main()
