from check_permutations_1_2 import check_permutation

TEST_CASES = {
    "identical strings": {
        "input": {"w1": "hello", "w2": "hello"},
        "expected": True
    },
}

if __name__ == '__main__':
    for tc_name, tc in TEST_CASES.items():
        expected = tc["expected"]
        assert check_permutation(**tc["input"]) == expected
    print("success")
