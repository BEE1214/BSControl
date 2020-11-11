##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-11-10 -=##
##=================================##

import threading


class muthread(threading.Thread):
    """
    Class for multithreading.
    """
    def __init__(self, aID, aCounter):
        """
        Constructor
        """
        threading.Thread.__init__(self)
        self.ThreadID = aID
        self.Counter = aCounter

    def run(self):
        """
        Run
        """
        pass