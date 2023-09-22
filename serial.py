"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.sec = start

    def generate(self):
        """Returns the next sequence value"""
        self.sec += 1
        return self.sec - 1

    def reset(self):
        """Restarts the sequence"""

        self.sec = self.start