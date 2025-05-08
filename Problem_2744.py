class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        distinct_words = set()

        for word in words:
            reversed_word = word[::-1]
            if reversed_word in distinct_words:
                distinct_words.remove(reversed_word)
                count+=1
            else:
                distinct_words.add(word)

        return count