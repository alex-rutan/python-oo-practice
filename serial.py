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
        '''takes in start integer, sets current counter value'''
        self.start = start
        self.last_number = start - 1

    def generate(self):
        '''increases current count value, returns the current count'''
        self.last_number += 1
        return self.last_number 

    def reset(self):
        '''resets the current count value back to the original start, start - 1'''
        self.last_number = self.start - 1
        
    

