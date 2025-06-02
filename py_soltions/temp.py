def one_way(s1: str, s2: str) -> int:
    s1_chars = {}
    additions = 0
    for c in s1:
        s1_chars[c] = s1_chars.get(c, 0) + 1
    for c in s2:
        if c not in s1_chars or s1_chars.get(c) == 0:
            if additions >= 1:
                return False
            additions += 1
            continue
        s1_chars[c] = s1_chars[c] - 1
    removals = sum(s1_chars.values())
    return additions <= 1 and removals <= 1





