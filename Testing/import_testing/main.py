# import my_function
import my_function

# import function into 'local' namespace
from my_function import foo


def main():
    my_function.foo()
    foo()


main()