"""
Solution of Vowel Spellchecker
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/vowel-spellchecker/description/
"""

from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_match = set(wordlist)  # stores exact matches
        capital_match = (
            {}
        )  # stores capitalisation issues {lowered_word:[word1, word2, ...]}
        vowel_match = {}  # {word with vowel replaced with '_':[list of such words]}
        vowels = {"a", "e", "i", "o", "u"}

        def replace_vowels(word):
            chars = [char if char not in vowels else "_" for char in word]
            return "".join(chars)

        for word in wordlist:
            lowered = word.lower()
            # Only need to store first occurence as the rule is to retrieve the first
            # word that match if case-insensitive
            if lowered not in capital_match:
                capital_match[lowered] = word

            # replace all vowels in word with '_'
            replaced_vowels = replace_vowels(lowered)

            if replaced_vowels != lowered:
                # Similar to capital match case
                if replaced_vowels not in vowel_match:
                    vowel_match[replaced_vowels] = word
        result = []

        for query in queries:
            # Check exact match
            if query in exact_match:
                result.append(query)
                continue
            lowered = query.lower()
            # Check matches up to capitalisation
            if lowered in capital_match:
                result.append(capital_match[lowered])
                continue
            # Check matches up to vowel errors
            replaced_vowels = replace_vowels(lowered)
            if replaced_vowels in vowel_match:
                result.append(vowel_match[replaced_vowels])
            else:
                result.append("")
        return result
