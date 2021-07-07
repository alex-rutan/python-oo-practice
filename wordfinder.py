from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        """Initialize taking in a file path
        creating a words attribute which is a list of words
        from the file read. Then it prints how many words
        were read from the file."""
        self.words = self.get_words(file_path)

        self.printWordsRead()

    def get_words(self, file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    
    def printWordsRead(self):
        """Prints a count of how many words are in this instance of WordFinder"""
        print(f"{len(self.words)} words read")
        
    def random(self):
        """returns a single random word from the words attribute."""
        return choice(self.words)
        


class SpecialWordFinder(WordFinder):
    '''finds random words from file with listed words, 
    while skipping blank lines and lines that start with "#" '''
    
    def get_words(self, file_path):
        with open(file_path, "r") as file:
            return [line[:-1] for line in file if line.strip() and line[0] != "#"] 