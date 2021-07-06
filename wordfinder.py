from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        """Initialize taking in a file path
        creating a words attribute which is a list of words
        from the file read. Then it prints how many words
        were read from the file."""
        self.words = []
        with open(file_path, "r") as file:
            for line in file:
                self.words.append(line[:-1])
        
        self.printWordsRead()
        
    def printWordsRead(self):
        """Prints a count of how many words are in this instance of WordFider"""
        print(f"{len(self.words)} words read")
        
    def random(self):
        """returns a single random word from the words attribute."""
        return choice(self.words)
        