# https://neetcode.io/problems/longest-repeating-substring-with-replacement
import typing


def _get_most_freq_char(freq: typing.Dict[str, int]) -> str:
    res = None
    curr_max_count = 0
    for char, count in freq.items():
        if count > curr_max_count:
            res = char
            curr_max_count = count
    return res


def _count_replacements(freq: typing.Dict[str, int], most_freq_char):
    res = 0
    for char, count in freq.items():
        if char == most_freq_char:
            continue
        res += count
    return res


def _can_expand_to_right(k, freq: typing.Dict[str, int], added_char):
    most_freq_char = _get_most_freq_char(freq)
    if _count_replacements(freq, most_freq_char) == k and most_freq_char == added_char:
        return True
    return _count_replacements(freq, most_freq_char) < k


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0 # inclusive pointer
        window_end = 1 # exclusive pointer
        freq = {s[0]: 1}
        max_window = 1
        while window_end < len(s):
            while window_end < len(s) and _can_expand_to_right(k, freq, s[window_end]):
                window_end += 1
                max_window = max(max_window, window_end - window_start)
                added_char = s[window_end - 1]
                freq[added_char] = freq.get(added_char, 0) + 1
            removed_char = s[window_start]
            if removed_char in freq:
                freq[removed_char] -= 1
                if freq[removed_char] == 0:
                    del freq[removed_char]
            window_start += 1
            if window_start == window_end:
                # maintain minimal window of size 1
                window_end += 1
                added_char = s[window_end - 1]
                freq[added_char] = freq.get(added_char, 0) + 1

        return max_window

if __name__ == '__main__':
    s = Solution()
    print(s.characterReplacement(s = "ABAA", k = 0))