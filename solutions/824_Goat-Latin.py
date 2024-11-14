class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        res = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"

            word += "a" * (i + 1)
            res.append(word)

        return " ".join(res)
