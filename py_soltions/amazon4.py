

def getMinOperations(weights, distances):
    # Create array to track positions
    positions = list(range(len(weights)))
    operations = 0

    while True:
        made_swap = False

        # Iterate through array from right to left (heaviest to lightest)
        for i in reversed(range(len(weights) - 1)):
            current_pos = positions[i]
            next_pos = positions[i + 1]

            # If weights need to be swapped
            if weights[current_pos] > weights[next_pos]:
                made_swap = True

                # Calculate how many steps can be taken
                steps_needed = next_pos - current_pos
                max_steps = min(distances[current_pos], steps_needed)

                if max_steps > 0:
                    # Move the point
                    positions[i] += max_steps
                    operations += 1

        # If no swaps were made, array is sorted
        if not made_swap:
            break

    return operations


# Test function with the example case
def test_sorting_algorithm():
    # Test case from the problem
    # weights = [3, 6, 5, 1]
    # distances = [4, 3, 2, 1]
    #
    # result = getMinOperations(weights, distances)
    # print(f"Number of operations required: {result}")
    #
    # # Additional test cases
    # test_cases = [
    #     {
    #         "weights": [1, 2, 3, 4],  # Already sorted
    #         "distances": [1, 1, 1, 1],
    #     },
    #     {
    #         "weights": [4, 3, 2, 1],  # Reverse sorted
    #         "distances": [1, 1, 1, 1],
    #     },
    #     {
    #         "weights": [2, 1, 4, 3],  # Random order
    #         "distances": [2, 2, 2, 2],
    #     }
    # ]
    #
    # for i, test in enumerate(test_cases, 1):
    #     result = getMinOperations(test["weights"], test["distances"])
    #     print(f"\nTest case {i}:")
    #     print(f"Weights: {test['weights']}")
    #     print(f"Distances: {test['distances']}")
    #     print(f"Operations required: {result}")

    res = getMinOperations([3,6,5,1], [4,3,2,1])
    assert res == 5, res


if __name__ == "__main__":
    test_sorting_algorithm()