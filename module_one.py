# Python intepreter sets "special variables", one of which is __name__
# Python will ssign the __name__ variable to the value of "__main__" if it's 
# the initial module being run

# y?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

import module_two

def main():
    print("Hello")

if __name__ == '__main__':
    main()