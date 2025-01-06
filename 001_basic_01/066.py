"""

Write a Python program to calculate the body mass index.

Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women.

The input height is expected to be in feet
The input weight is expected to be in kg

BMI = w (kg) / h^2 (feet)
"""


def main():
    feet, kg = [float(_) for _ in input("Enter the height in feet and weight in kg as: 'h w' ").split()]
    print(f"Body Mass Index (BMI): {kg / pow(feet, 2): 3f}")


if __name__ == "__main__":
    main()
