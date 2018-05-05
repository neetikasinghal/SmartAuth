import os

from utils import interface


def register_test_users():
    filenames=['avinash','dhivya','kavitha','kpoornima','neetika','poornima','rashmi','santhosh','sidharth','arun']
    for filename in filenames:
        i = interface.SmartAuthInterface()
        i.enrollModelling(filename)

def validate_test_users():
    filenames=['avinash','dhivya','kavitha','kpoornima','neetika','santhosh','sidharth','arun']
    for filename in filenames:
        i = interface.SmartAuthInterface()
        i.authenticateModelling(filename, "authenticate")


if __name__ == '__main__':
    os.chdir('../')
    # accuracy(os.path.abspath(os.curdir))
    # register_test_users()
    validate_test_users()

