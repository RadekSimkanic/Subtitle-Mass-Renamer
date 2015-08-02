#UTF-8
import sys

INFORMATION = 0
WARNING = 1
ERROR = 2
EXCEPTION = 3
DONE = 4
SYSTEM_ERROR = 5 # programmer, program or internal error

def message(type, text, error = None):
    if type == INFORMATION:
        print("Info: %s" % text)
    elif type == WARNING:
        print("\033[33mWarning:\033[0m %s" % text)
    elif type == ERROR:
        print("\033[31;1mError:\033[0m %s" % text)
        sys.exit()
    elif type == SYSTEM_ERROR:
        raise error, text
    elif type == EXCEPTION:
        print("\033[41;1mEXCEPTION:\033[0m %s" % text)
    elif type == DONE:
        print("\033[32;1m %s \033[0m" % text)