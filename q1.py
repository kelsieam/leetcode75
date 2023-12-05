class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_string = ""
        
        index1 = 0
        index2 = 0

        while index1 < len(word1) and index2 < len(word2):
            final_string += word1[index1] + word2[index2]
            index1 += 1
            index2 += 1

        final_string += word1[index1:]
        final_string += word2[index2:]
        
        return final_string
