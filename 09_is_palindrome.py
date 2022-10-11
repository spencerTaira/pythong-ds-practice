def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    listPhrase = list(phrase.lower())
    filteredPhrase = [char for char in listPhrase if char != ' ']
    tempPhrase = filteredPhrase.copy()
    filteredPhrase.reverse()
    if tempPhrase == filteredPhrase:
        return True
    return False