import itertools

def power_set_rec(s: set) -> set:
    if not s:
        return {frozenset()}
    return set(_power_set_rec(s))

def _power_set_rec(s: set) -> set:
    if not s:
        return {frozenset([])}
    res = {frozenset(s)}
    for elem in s:
        res = res.union(_power_set_rec(s - {elem}))
    return frozenset(res)


def _add_element_to_power_set(res: set[frozenset], added_element):
    for subset in res.copy():
        res.add(frozenset(subset | {added_element}))
    return res


def power_set(s: set) -> set:
    res = {frozenset()}
    for elem in s:
        res.add(frozenset({elem}))
        res = _add_element_to_power_set(res, elem)
    return res

def power_set_v1_incorrect(s: set) -> set:
    s = list(s)
    res = set()
    for subset_perm in itertools.product([True, False], repeat=len(s)):
        subset = set()
        for i in range(len(s)):
            if subset_perm[i]:
                subset.add(s[i])
        res.add(frozenset(subset))
    return res

if __name__ == '__main__':
    print(power_set_rec({1}))