"""

Write a Python program to determine the profiling of Python programs.
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
These statistics can be formatted into reports via the pstats module.

"cProfile" and "profile" provide deterministic profiling of Python programs.

"""

import cProfile


VAR = 0


def increment_global_var():
    global VAR
    VAR += 1


def loop():
    for _ in range(10000):
        increment_global_var()


def main():
    cProfile.run("loop()")

    """
    The first line indicates that x calls were monitored. Of those calls, y were primitive, meaning that the 
    call was not induced via recursion. 
    The next line: Ordered by: indicates the output is sorted by some metric. 
    
    The column headings include:

        ncalls
            for the number of calls.
        
        tottime
            for the total time spent in the given function (and excluding time made in calls to sub-functions)
        
        percall
            is the quotient of tottime divided by ncalls
        
        cumtime
            is the cumulative time spent in this and all subfunctions (from invocation till exit). This figure is 
            accurate even for recursive functions.
        
        percall
        is the quotient of cumtime divided by primitive calls
        
        filename:lineno(function)
            provides the respective data of each function
    """


if __name__ == "__main__":
    main()
