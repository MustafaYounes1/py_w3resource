"""

Write a Python program that creates a list of tuples, each containing a city name and its population. Use the filter
function to extract cities with a population greater than 2 million.

cities = [
    ("New York", 8_500_000),
    ("Los Angeles", 4_000_000),
    ("Chicago", 2_700_000),
    ("Houston", 2_300_000),
    ("Phoenix", 1_600_000),
    ("Philadelphia", 1_500_000),
    ("San Antonio", 1_500_000),
]

[('New York', 8500000), ('Los Angeles', 4000000), ('Chicago', 2700000), ('Houston', 2300000)]

"""


def main():
    cities = [
        ("New York", 8_500_000),
        ("Los Angeles", 4_000_000),
        ("Chicago", 2_700_000),
        ("Houston", 2_300_000),
        ("Phoenix", 1_600_000),
        ("Philadelphia", 1_500_000),
        ("San Antonio", 1_500_000),
    ]

    print(list(filter(lambda _: _[1] > 2e6, cities)))


if __name__ == "__main__":
    main()
