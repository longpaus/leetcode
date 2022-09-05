class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        longest = 0
        for s in sentences:
            count = 0
            for l in s:
                if l == ' ':
                    count += 1
            if count + 1 > longest:
                longest = count + 1
        return longest
        