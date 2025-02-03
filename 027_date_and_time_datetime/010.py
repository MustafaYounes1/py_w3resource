"""

Write a Python program to add 5 seconds to the current time.

Current time:   19:03:24.771686
+5 seconds:     19:03:29.771686

"""

from datetime import datetime, timedelta


def main():
    curr_dt = datetime.now()

    print(f"Current time:   {curr_dt.time()}")
    print(f"+5 seconds:     {(curr_dt + timedelta(seconds=5)).time()}")


if __name__ == "__main__":
    main()
