class Anagram:
    def __init__(self, word):
        self.letters = sorted([letter for letter in word])

    def match(self, letters):
        match_words = []

        for word in letters:
            if sorted([letter for letter in word]) == self.letters:
                match_words.append(word)

        return match_words