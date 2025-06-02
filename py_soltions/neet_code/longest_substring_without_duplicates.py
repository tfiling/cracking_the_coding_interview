# https://neetcode.io/problems/longest-substring-without-duplicates

def longest_substring_without_duplicates(s: str) -> int:
    res = 0
    curr_substring = {s[0]}
    start_idx = 0
    end_idx = 1
    while end_idx < len(s):
        if s[end_idx] in curr_substring:
            print(s[start_idx:end_idx])
            res = max(res, len(curr_substring))
            while s[end_idx] in curr_substring:
                curr_substring.remove(s[start_idx])
                start_idx += 1
        curr_substring.add(s[end_idx])
        end_idx += 1
    res = max(res, len(curr_substring))
    return res

if __name__ == '__main__':
    print(longest_substring_without_duplicates("zxyzxyz"))
