PROMPT = """Given the above analysis of the question - generate test cases. Make sure each test case tests a different aspect of future solutions and is correct.
Return the response as a minified JSON in the following format:
[{"name":"first test case","explanation":"this test case checks the edge case where ...","arguments":{"first_arg":1,"second_arg":[1,2,3],"third_arg":"a string argument"},"expected":8}]"""

# https://python-jsonschema.readthedocs.io/en/stable/
EXPECTED_RESP_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "explanation": {"type": "string"},
            "arguments": {
                "type": "object",
                "minProperties": 1  # Requires at least one property
            },
            "expected": {}  # Allows any type for expected result
        },
        "required": ["name", "explanation", "arguments", "expected"]
    }
}
