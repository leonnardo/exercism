def distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))
