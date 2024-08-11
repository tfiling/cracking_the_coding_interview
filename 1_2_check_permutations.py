def check_permutation(w1: str, w2: str) -> bool:
    seen = {}
    for c in w1:
        new_count = seen.get(c, 0) + 1
        seen[c] = new_count
    for c in w2:
        new_count = seen.get(c, 0) - 1
        if new_count < 0:
            return False
        if new_count == 0:
            del seen[c]
        else:
            seen[c] = new_count
    return len(seen) == 0

test_cases = {
    "identical strings": {
        "input": ("hello", "hello"),
        "expected": True
    },
    "permutation": {
        "input": ("abc", "cab"),
        "expected": True
    },
    "different lengths": {
        "input": ("hello", "hell"),
        "expected": False
    },
    "same letters, different counts": {
        "input": ("aab", "aba"),
        "expected": True
    },
    "empty strings": {
        "input": ("", ""),
        "expected": True
    },
    "case sensitivity": {
        "input": ("God", "dog"),
        "expected": False
    },
    "spaces matter": {
        "input": ("god   ", "dog"),
        "expected": False
    },
    "unicode characters": {
        "input": ("résumé", "émusér"),
        "expected": True
    },
    "non-permutation": {
        "input": ("hello", "world"),
        "expected": False
    },
    "single character": {
        "input": ("a", "a"),
        "expected": True
    }
}

if __name__ == '__main__':
    for tc_name, tc in test_cases.items():
        w1, w2 = tc["input"]
        expected = tc["expected"]
        assert check_permutation(w1, w2) == expected
    print("success")
