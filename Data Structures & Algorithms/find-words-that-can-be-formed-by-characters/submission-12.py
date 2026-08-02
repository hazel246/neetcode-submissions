from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count=Counter(chars)
        count=0

        for word in words:
            word_count=Counter(word)

            can_make=True

            for c in word_count:
                if word_count[c]>chars_count[c]:
                    can_make=False
                    break

            if can_make:
                count+=len(word)

        return count



        

        