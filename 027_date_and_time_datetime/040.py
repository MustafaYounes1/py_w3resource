"""

Write a Python program to get the current date and time information.

Time in seconds since the epoch:    1738599293.296373
Current date and time:              2025-02-03 19:14:53.296373
Alternate date and time:            25-02-03-19-14
Current year:                       2025
Month of year:                      February
Week number of the year:            05
Weekday of the week:                0
Day of year:                        034
Day of the month:                   03
Day of week:                        Monday

"""

from datetime import datetime


def main():
    dt = datetime.now()

    print(f"Time in seconds since the epoch:    {dt.timestamp()}")
    print(f"Current date and time:              {dt}")
    print(f"Alternate date and time:            {dt.strftime('%y-%m-%d-%H-%M')}")
    print(f"Current year:                       {dt.year}")
    print(f"Month of year:                      {dt.strftime('%B')}")
    print(f"Week number of the year:            {dt.strftime('%W')}")
    print(f"Weekday of the week:                {dt.weekday()}")
    print(f"Day of year:                        {dt.strftime('%j')}")
    print(f"Day of the month:                   {dt.strftime('%d')}")
    print(f"Day of week:                        {dt.strftime('%A')}")


if __name__ == "__main__":
    main()
