"""

Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = (f-32) / 9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius

"""


def convert_d(d, u):
    if u == "c":
        return round((d - 32) * 5 / 9)

    elif u == "f":
        return round(d * 9 / 5 + 32)

    else:
        raise ValueError("The expected units are: (c, f)")


def main():
    c_degrees, f_degrees = 60, 45
    print(f"{c_degrees:3d} C is {convert_d(c_degrees, 'f'):3d} F")
    print(f"{c_degrees:3d} C is {convert_d(f_degrees, 'c'):3d} C")


if __name__ == "__main__":
    main()
