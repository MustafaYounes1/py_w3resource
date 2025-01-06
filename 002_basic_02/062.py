"""

Write a Python program to find the number of combinations that satisfy p + q + r + s = n where n is a given number <=
4000 and p, q, r, s are between 0 and 1000.

Input a positive integer: (ctrl+d to exit)  252
Number of combinations of a,b,c,d:          2731135

"""


def main():
    n = int(input("Enter an integer: "))

    num_of_comb = 0
    for a in range(max(0, n - 3000), min(n, 1000) + 1):
        for b in range(max(0, n - a - 2000), min(n - a, 1000) + 1):
            for c in range(max(0, n - a - b - 1000), min(n - a - b, 1000) + 1):
                s = n - a - b - c
                if 0 <= s <= 1000:
                    num_of_comb += 1

    print(num_of_comb)

    """ Another solution
    # Import the Counter class from the collections module
    from collections import Counter
    
    # Print statement to instruct the user to input a positive integer (ctrl+d to exit)
    print("Input a positive integer: (ctrl+d to exit)")
    
    # Create a Counter object to store pairs of integers and their counts
    pair_dict = Counter()
    
    # Assign counts to pairs of integers based on their minimum and maximum values
    for i in range(2001):
        pair_dict[i] = min(i, 2000 - i) + 1
    
    # Continuous loop to read input until EOFError (ctrl+d) is encountered
    while True:
        try:
            # Read a positive integer from the user
            n = int(input())
            
            # Initialize a variable to store the number of combinations
            ans = 0
    
            # Iterate over possible values of 'i' and calculate combinations
            for i in range(n + 1):
                ans += pair_dict[i] * pair_dict[n - i]
            
            # Print the number of combinations of a, b, c, d
            print("Number of combinations of a, b, c, d:", ans)
    
        # Break the loop when EOFError is encountered
        except EOFError:
            break
    
    """


if __name__ == "__main__":
    main()
