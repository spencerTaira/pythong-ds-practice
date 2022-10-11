def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    str = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.isupper():
                str += char.lower()
            if char.islower():
                str += char.upper()
        else:
            str += char

    return str


