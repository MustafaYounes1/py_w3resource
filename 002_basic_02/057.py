"""

There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green. Blue represents
the sea, and green represents the land. When two green squares are in contact with the top and bottom, or right and
left, they are said to be ground. The area created by only one green square is called "island". For example, there
are five islands in the figure below.

Write a Python program to read the mass data and find the number of islands.

Input:
A single data set is represented by 10 rows of 10 numbers representing green squares as 1 and blue squares as zeros.

1100000111
1000000111
0000000111
0010001000
0000011100
0000111110
0001111111
1000111110
1100011100
1110001000

Number of islands:  5

"""


def process_row(row):
    i0 = -1
    found_islands = []
    found_1 = False

    for idx, sqr in enumerate(row):
        if sqr == "1" and not found_1:
            i0 = idx
            found_1 = True

        elif sqr == "1" and found_1:
            if idx == (len(row) - 1):
                found_islands.append([i0, idx])
                i0 = -1
                found_1 = False

        elif sqr == "0" and found_1:
            found_islands.append([i0, idx - 1])
            i0 = -1
            found_1 = False

        else:
            pass

    return found_islands


def detect_num_of_islands(data):
    # store the last detected islands in order to check for connections in the subsequent rows
    tmp = process_row(data[0])
    num_of_islands = len(tmp)
    for row in data[1:]:
        curr_islands = process_row(row)

        for curr_isl in curr_islands:
            for pre_island in tmp:
                s1 = set(range(curr_isl[0], curr_isl[1] + 1))
                s2 = set(range(pre_island[0], pre_island[1] + 1))
                if s1 & s2:
                    # current island is connected to one of the previously detected islands => don't increment the
                    # islands counter for this island
                    break
            else:
                num_of_islands += 1

        tmp = curr_islands

    return num_of_islands


"""
    Another good solution:
    
# Initialize counter variable 'c' to 0
c = 0

# Define a recursive function 'f' with parameters x, y, and z
def f(x, y, z):
    # Check conditions for valid coordinates and if the square is part of the island ('1')
    if 0 <= y < 10 and 0 <= z < 10 and x[z][y] == '1':
        # Change the square to '0' to mark it as visited
        x[z][y] = '0'
        # Recursively call 'f' for neighboring squares
        for dy, dz in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            f(x, y + dy, z + dz)

# Print a statement instructing the user to input 10 rows of 10 numbers representing the island and sea
print("Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros") 

# Run an infinite loop
while 1:
    try:
        # If 'c' is not 0, prompt the user to input (used for multiple test cases)
        if c:
            input()
    except:
        # Break the loop if an exception occurs (typically EOF)
        break

    # Read 10 rows of 10 characters each to represent the island and sea
    x = [list(input()) for _ in [0] * 10]
    # Set 'c' to 1 to indicate subsequent iterations
    c = 1
    # Initialize counter 'b' to 0 to count the number of islands
    b = 0

    # Nested loops to iterate through each square in the grid
    for i in range(10):
        for j in range(10):
            # Check if the square is part of an island ('1')
            if x[j][i] == '1':
                # Increment the island counter 'b'
                b += 1
                # Call the recursive function 'f' to mark the connected island squares
                f(x, i, j)

    # Print the number of islands in the input grid
    print("Number of islands:")     
    print(b)
"""


def main():
    # hardcoded data
    data = [
        "1100000111",
        "1000000111",
        "0000000111",
        "0010001000",
        "0000011100",
        "0000111110",
        "0001111111",
        "1000111110",
        "1100011100",
        "1110001000"
    ]

    # prompt user to provide the data
    # print("Input 10 rows where each row has only 10 characters (1s and 0s): ")
    #
    # data = []
    # for _ in range(10):
    #     r = input("").strip()
    #     assert set(r) in ({"0"}, {"1"}, {"0", "1"}) and len(r) == 10, "invalid input"

    print(detect_num_of_islands(data))


if __name__ == "__main__":
    main()
