PROMPT="""Analyze the following technical question, explain the given examples, and suggest the best possible solution's run and memory complexity.
Return the response as a minified JSON in the following format:
{{"explanation":"in this question we are asked to ...","examples":[{{"Example 1":"In this example we get X, apply the operations Y1, Y2, Y3 and that's how we get the output Z"}},{{"Example 2":"These are the steps that are applied to the inputs to get the output: ..."}}],"best_achievable_runtime":"O(N)","best_achievable_memory":"O(1)","argument_names":["first_arg","second_arg","third_arg"]}}

The Question:
{question}

Solution template:
{solution_template}
"""
