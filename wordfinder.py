"""Word Finder: finds random words from a dictionary."""

from random import randrange

class WordFinder:
        
    def __init__(self, path):
        file = open(path, "r")
        self.words = self.parseLine(file)
        file.close()
        print( f'{len(self.words)} words read' )

    def parseLine(self, file):
        return [word.strip() for word in file]
    
    def random(self):
        return self.words[randrange(len(self.words))]

class SpecialWordFinder(WordFinder):
        
        def __init__(self, path):
            super().__init__(path)

        def parseLine(self, file):
            return [word.strip() for word in file if not word.isspace() and not word.startswith("#")]