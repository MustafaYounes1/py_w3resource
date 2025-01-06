"""

Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days

"""


def main():
    month = input("Enter a month: ")

    if month.lower() == "february":
        print("No. of days: 28/29 days")

    elif month.lower() in ("january", "march", "may", "july", "august", "october", "december"):
        print("No. of days: 31 days")

    else:
        print("No. of days: 30 days")

if __name__ == "__main__":
    main()
