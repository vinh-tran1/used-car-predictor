"""
program: runserver.py
by: Vinh and Nikhil

description: runs flask app on specified port

"""
import argparse
import sys
from app import app

def get_port():
    """ parse the command line arguments for port
        store argument as variable
    """
    # define positional arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('port', metavar='port', type=int,
                    help='the port at which the server should listen')

    args = parser.parse_args()
    port =  args.port

    # no need to explicitly error check, argparse does it for us
    return port

def main():
    """ main function to start flask app
    """

    # might need to check if valid port
    port = get_port()

    try:
        app.run(host='0.0.0.0', port=port, debug=True)

    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
