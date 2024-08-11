import math


def one_way(w1, w2) -> bool:
    if math.fabs(len(w1) - len(w2)) > 1:
        return False
    if len(w1) == len(w2):
        # replace or no edits
        replaced_count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                replaced_count += 1
                if replaced_count > 1:
                    return False
        # Counted a single replace
        return True
    else:
        # One removal or insert
        diff = 0
        if len(w1) > len(w2):
            long, short = w1, w2
        else:
            long, short = w2, w1
        for i in range(len(short)):
            if long[i + diff] != short[i]:
                if diff == 1:
                    # This is the 2nd addition/ removal detected
                    return False
                diff = 1
        return True


test_cases = {
    "example_1_replace": {
        "input": ("pale", "ple"),
        "expected": True,
        "description": "Replace 'a' with 'l'"
    },
    "example_2_insert": {
        "input": ("pales", "pale"),
        "expected": True,
        "description": "Remove 's' from first string"
    },
    "example_3_replace": {
        "input": ("pale", "bale"),
        "expected": True,
        "description": "Replace 'p' with 'b'"
    },
    "example_4_false": {
        "input": ("pale", "bake"),
        "expected": False,
        "description": "More than one edit away"
    },
    "no_edit": {
        "input": ("same", "same"),
        "expected": True,
        "description": "Identical strings"
    },
    "insert_middle": {
        "input": ("cat", "cart"),
        "expected": True,
        "description": "Insert 'r' in the middle"
    },
    "remove_end": {
        "input": ("carts", "cart"),
        "expected": True,
        "description": "Remove 's' from the end"
    },
    "replace_case": {
        "input": ("Cat", "cat"),
        "expected": True,
        "description": "Replace uppercase with lowercase"
    },
    "two_inserts": {
        "input": ("cat", "carts"),
        "expected": False,
        "description": "Two inserts needed"
    },
    "empty_and_one": {
        "input": ("", "a"),
        "expected": True,
        "description": "Empty string and single character"
    },
    "empty_and_two": {
        "input": ("", "ab"),
        "expected": False,
        "description": "Empty string and two characters"
    },
    "long_strings_one_away": {
        "input": ("longerstring", "longerstrina"),
        "expected": True,
        "description": "Change last character in longer string"
    },
    "long_strings_not_one_away": {
        "input": ("longerstring", "shorterstring"),
        "expected": False,
        "description": "Long strings with multiple differences"
    },
    "unicode_replace": {
        "input": ("café", "cafe"),
        "expected": True,
        "description": "Replace accented character"
    },
    "space_difference": {
        "input": ("a b", "ab"),
        "expected": True,
        "description": "Remove space"
    }
}

if __name__ == '__main__':
    conclusion = "success"
    for tc_name, tc in test_cases.items():
        w1, w2 = tc["input"]
        expected = tc["expected"]
        if one_way(w1, w2) != expected:
            print(f"{tc_name} failed")
            conclusion = "failure"
    print(conclusion)
