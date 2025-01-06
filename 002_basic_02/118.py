"""

In multiprocessing, processes are spawned by creating a Process object. Write a Python program to show the
individual process IDs (parent process, process ID etc.) involved.

Sample Output:
Main line
module name: __main__
parent process: 23967
process id: 27986
function f
module name: __main__
parent process: 27986
process id: 27987
hello bob

"""

# Import the 'Process' class from the 'multiprocessing' module.
from multiprocessing import Process

# Import the 'os' module for interacting with the operating system.
import os


# Define a function 'info' to print process-related information.
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


# Define a function 'f' that takes a name as an argument.
def f(name):
    # Call the 'info' function to print process-related information.
    info('function f')
    # Print a greeting using the provided name.
    print('hello', name)


def main():
    # Call the 'info' function to print process-related information for the main process.
    info('Main line')

    print("=" * 25)

    # Create a new 'Process' object, specifying the target function 'f' and its arguments.
    p = Process(target=f, args=('Mustafa',))

    # Start the new process.
    p.start()

    # Wait for the child process to complete before continuing.
    p.join()


if __name__ == "__main__":
    main()
