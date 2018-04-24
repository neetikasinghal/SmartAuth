import argparse

from utils import interface

def  get_args():

    parser = argparse.ArgumentParser(description="Smart Authenticator",
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-a', '--action',
                       help=' \'register\' a new user or \'authenticate\' an existing user',
                       required=True)
    parser.add_argument('-i', '--input',
                       help='username',
                       required=True)
    return parser.parse_args()


def action_authenticate(user,path):
    i = interface.SmartAuthInterface()
    i.authenticateinterface(user,path)

def action_enroll(path):
    i = interface.SmartAuthInterface()
    i.enrollinterface(path)

def action_initialize():
    i = interface.SmartAuthInterface()
    i.initialize()

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
    elif((action=='setup')):
        print("Initializing the UBM...")
        action_initialize()
    
