import argparse

from utils import interface

def  get_args():
    epilog = """
    Enter the text that you want to display
    """
    parser = argparse.ArgumentParser(description="Smart Authenticator", epilog=epilog,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-a', '--action',
                       help='Use register to Register a new user or authenticate to Authenticate an existing user',
                       required=True)
    parser.add_argument('-i', '--input',
                       help='The folder path / path to the file for the input signals',
                       required=True)
    return parser.parse_args()


def action_authenticate(user,path):
    i = interface.SmartAuthInterface()
    i.authenticateinterface(user,path)

def action_enroll(path):
    i = interface.SmartAuthInterface()
    i.enrollinterface(path)

if __name__ == '__main__':
    global args
    args = get_args()

    action = args.action
    if action == 'register':
        print('Registering...')
        action_enroll(args.input)
    elif ((action == 'authenticate') | (action == 'auth')):
        print('Authenticating...')
        action_authenticate(args.input,"authenticate")
    
