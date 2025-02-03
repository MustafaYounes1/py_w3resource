"""

Write a Python script to display the various Date Time formats
    a) Current date and time
    b) Current year
    c) Month of year                (As a string)
    d) Week number of the year
    e) Weekday of the week
    f) Day of year
    g) Day of the month
    h) Day of week                  (As a string)


Current date and time:      2025-02-02 17:48:59.480494
Current year:               2025
Month of year:              February
Week number of the year:    04
Weekday of the week:        0
Day of year:                033
Day of the month:           2
Day of week:                Sunday

"""

from datetime import datetime


def main():
    now = datetime.today()

    print(f"Current date and time:      {now}")
    print(f"Current year:               {now.year}")
    print(f"Month of year:              {now.strftime('%B')}")
    print(f"Week number of the year:    {now.strftime('%W')}")
    print(f"Weekday of the week:        {now.strftime('%w')}")
    print(f"Day of year:                {now.strftime('%j')}")
    print(f"Day of the month:           {now.day}")
    print(f"Day of week:                {now.strftime('%A')}")


if __name__ == "__main__":
    main()
