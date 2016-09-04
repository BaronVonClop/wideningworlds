"""
ANSI

ANSI utils

"""


def syntax_error(caller, command):
    """Informs the caller of the syntax error"""
    caller.msg("Syntax error. Type 'help " + command + "' for help.")
            
