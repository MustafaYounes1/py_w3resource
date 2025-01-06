"""

Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)

Sample Output :
===============
The examination will start from : 11 / 12 / 2014

"""

from datetime import date


def main():
    xam_st_date = (11, 12, 2014)
    # print("The examination will start from : %i / %i / %i" % exam_st_date)
    schedule = date(day=xam_st_date[0], month=xam_st_date[1], year=xam_st_date[2])
    print(schedule.strftime("%d / %m / %Y"))


if __name__ == "__main__":
    main()
