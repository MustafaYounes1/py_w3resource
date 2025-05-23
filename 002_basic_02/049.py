"""

Write a Python program that reads the two adjoining sides and the diagonal of a parallelogram and checks whether
the parallelogram is a rectangle or a rhombus.

According to Wikipedia-
parallelograms: In Euclidean geometry, a parallelogram is a simple (non-self-intersecting) quadrilateral with two
pairs of parallel sides. The opposite or facing sides of a parallelogram are of equal length and the opposite angles
of a parallelogram are of equal measure.

rectangles: In Euclidean plane geometry, a rectangle is a quadrilateral with four right angles. It can also be defined
as an equiangular quadrilateral, since equiangular means that all of its angles are equal (360°/4 = 90°). It can also
be defined as a parallelogram containing a right angle.

rhombus: In plane Euclidean geometry, a rhombus (plural rhombi or rhombuses) is a simple (non-self-intersecting)
quadrilateral whose four sides all have the same length. Another name is equilateral quadrilateral, since equilateral
means that all of its sides are equal in length. The rhombus is often called a diamond, after the diamonds suit in
playing cards which resembles the projection of an octahedral diamond, or a lozenge, though the former sometimes
refers specifically to a rhombus with a 60° angle, and the latter sometimes refers specifically to a rhombus with
a 45° angle.

Input:
Two adjoined sides and the diagonal.
1 <= ai, bi, ci <= 1000, ai + bi > ci
Input two adjoined sides and the diagonal of a parallelogram (comma separated): 3,4,5
                                                                                This is a rectangle.

"""


def main():
    # Prompt the user to input two adjoined sides and the diagonal of a parallelogram (comma separated)
    print("Input two adjoined sides and the diagonal of a parallelogram (comma separated):")

    # Take user input for the sides and diagonal, and map to integers
    a, b, c = map(int, input().split(","))

    # Check if the parallelogram is a rectangle using the Pythagorean theorem
    if c ** 2 == a ** 2 + b ** 2:
        print("This is a rectangle.")

    # Check if the parallelogram is a rhombus by comparing the lengths of the adjoined sides
    if a == b:
        print("This is a rhombus.")


if __name__ == "__main__":
    main()
