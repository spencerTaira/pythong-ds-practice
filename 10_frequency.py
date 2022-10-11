def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """

    freq = {}

    for item in lst:
        freq[item] = (freq.get(item) or 0) + 1

    return freq.get(search_term, 0)