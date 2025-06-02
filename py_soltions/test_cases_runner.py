import typing

from py_soltions.group_anagrams import _group_anagrams

TEST_CASES = {
    "example 1": {
        "input": {
            "strs": ["act", "pots", "tops", "cat", "stop", "hat"]
        },
        "expected": [["hat"], ["act", "cat"], ["stop", "pots", "tops"]],
        "explanation": "Words are grouped based on their anagram equivalence."
    },
    "example 2": {
        "input": {
            "strs": ["x"]
        },
        "expected": [["x"]],
        "explanation": "A single character cannot form an anagram group with others."
    },
    "example 3": {
        "input": {
            "strs": [""]
        },
        "expected": [[""]],
        "explanation": "An empty string is grouped alone."
    },
    "example 4": {
        "input": {
            "strs": ["listen", "silent", "enlist", "google", "goggle", "inlets"]
        },
        "expected": [["listen", "silent", "enlist", "inlets"], ["google"], ["goggle"]],
        "explanation": "Grouping anagrams together, where 'listen', 'silent', 'enlist', and 'inlets' belong together."
    },
    "example 5": {
        "input": {
            "strs": ["abc", "bca", "cab", "xyz", "zyx", "yxz", "mn", "nm"]
        },
        "expected": [["abc", "bca", "cab"], ["xyz", "zyx", "yxz"], ["mn", "nm"]],
        "explanation": "Three different anagram groups are identified."
    },
    "example 6": {
        "input": {
            "strs": ["aaa", "aaa", "aaa"]
        },
        "expected": [["aaa", "aaa", "aaa"]],
        "explanation": "All identical words form a single anagram group."
    },
}

def run_examples(solution: typing.Callable, should_sort_res=False):
    for tc_name, tc in TEST_CASES.items():
        expected = tc["expected"]
        res = solution(**tc["input"])
        if should_sort_res:
            assert sorted(res) == sorted(expected), f"{tc_name}: {res} != {expected}[]"
        else:
            assert res == expected, f"{tc_name}: {res} != {expected}[]"

if __name__ == '__main__':
    run_examples(_group_anagrams)
    print("success")

