# https://neetcode.io/problems/string-encode-and-decode

from typing import List


def _escape_str(s: str) -> str:
    s = s.replace("\\", "\\\\")
    s = s.replace("\"", "\\\"")
    s = s.replace(",", "\\,")
    return s


def _unescape(s: str) -> str:
    s = s.replace("\\\"", "\"")
    s = s.replace("\\,", ",")
    s = s.replace("\\\\", "\\")
    return s


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"\"{_escape_str(s)}\","
        return res[:-1]

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        return [_unescape(w) for w in s[1:-1].split("\",\"")]


if __name__ == '__main__':
    s = Solution()
    print(s.decode(s.encode(["1,23","45,6","7,8,9"])))