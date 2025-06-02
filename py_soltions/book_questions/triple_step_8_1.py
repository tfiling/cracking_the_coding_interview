def triple_step(n: int) -> int:
    if n <= 0:
        return 0
    precalculated_sols = {
        1: 1,
        2: 2,
        3: 4,
        4: 7,
    }
    if n <= 4:
        return precalculated_sols[n]
    for k in range(5, n+1):
        precalculated_sols[k] = precalculated_sols[k-1] + precalculated_sols[k-2] + precalculated_sols[k-3]
    return precalculated_sols[n]