"""

Write a Python program to get the execution time of a Python method.

"""

import time

VAR = 1


def increment_global_var():
    global VAR
    VAR += 1


def loop():
    for _ in range(1_000_000):
        increment_global_var()


def main():
    """
    Return the time in seconds since the epoch as a floating-point number.

    The epoch is the point where the time starts, the return value of time.gmtime(0).
    It is January 1, 1970, 00:00:00 (UTC) on all platforms.

    The handling of leap seconds is platform dependent.
    A leap second is a one-second adjustment that is occasionally applied to Coordinated Universal Time (UTC),
    to accommodate the difference between precise time (International Atomic Time (TAI), as measured by atomic clocks)
    and imprecise observed solar time (UT1), which varies due to irregularities and long-term slowdown in the Earth's
    rotation.

    On Windows and most Unix systems, the leap seconds are not counted towards the time in seconds since the epoch.
    This is commonly referred to as Unix time.
    """

    srt = time.time()
    loop()
    end = time.time()
    print(f"Elapsed time after executing the loop function: {end - srt:5f} sec")


if __name__ == "__main__":
    main()
