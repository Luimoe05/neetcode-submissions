class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        first_word = {}
        second_word = {}
        for c in s:
            first_word[c] = first_word.get(c, 0) + 1

        for c in t:
            second_word[c] = second_word.get(c, 0) + 1

        
        return first_word == second_word