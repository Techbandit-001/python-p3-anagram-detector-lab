# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        base_sorted = sorted(self.word)
        return [
            candidate for candidate in word_list
            if sorted(candidate.lower()) == base_sorted and candidate.lower() != self.word
        ]

