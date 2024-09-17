class Anagram:
    def __init__(self, word):
        self.letters = sorted([letter for letter in word])