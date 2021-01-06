##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2021-01-04 -=##
##=================================##


class Error(Exception):
    """
    Base class for exceptions.
    """
    pass

class InputNotInInterval(Error):
    """
    Input is wrong number!
    """
    pass

class InputWrongLetter(Error):
    """
    Input is wrong letter!
    """
    pass

class InputWrong(Error):
    """
    Entered wrong character!
    """
    pass

class UnknownOS(Error):
    """
    Using unknown operating system.
    """
    pass
