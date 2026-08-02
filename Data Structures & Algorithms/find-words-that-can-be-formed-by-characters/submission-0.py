from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        answer = 0

        for word in words:
            word_count = Counter(word)

            if all(word_count[c] <= chars_count[c] for c in word_count):
                answer += len(word)

        return answer