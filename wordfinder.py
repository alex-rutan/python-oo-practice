from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        """Initialize WordFinder taking in a file path
        Makes a words attribute from words in the file
        Then it prints how many words were read from the file."""
        self.words = self.get_words(file_path)
        print(self.print_Words_Read())
        
    def __repr__(self):
        """instead of showing position in memory, shows how many words read"""
        return self.print_Words_Read()

    def get_words(self, file_path):
        """takes in a file path, returns a list of words
        from the file read."""
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    
    def print_Words_Read(self):
        """Prints a count of how many words are in this instance of WordFinder"""
        return f"{len(self.words)} words read"
        
    def random(self):
        """returns a single random word from the words attribute."""
        return choice(self.words)
        


class SpecialWordFinder(WordFinder):
    '''finds random words from file with listed words, 
    while skipping blank lines and lines that start with "#" '''
    
    def get_words(self, file_path):
        """takes in a file path, returns a list of words
        from the file read ignoring blank lines and line starting with #"""
        with open(file_path, "r") as file:
            return [line.strip() 
                for line in file 
                if line.strip() and line[0] != "#"] 