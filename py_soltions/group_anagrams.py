# https://neetcode.io/problems/anagram-groups
from typing import List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return _group_anagrams(strs)

def _group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = {}
    for word in strs:
        anagram_key = _calc_anagram_key(word)
        anagrams_lst = anagrams.get(anagram_key, [])
        anagrams_lst.append(word)
        anagrams[anagram_key] = anagrams_lst
    return list(anagrams.values())


def _calc_anagram_key(s: str) -> frozenset[Tuple[str,int]]:
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    return frozenset({(c,count) for c, count in char_count.items()})

