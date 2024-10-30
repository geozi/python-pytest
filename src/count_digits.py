def count(number):
    
    """ Counts the number of digits in an integer.

    Args:
        number (int): An integer provided by the caller.

    Returns:
        int: An integer representing the number of digits.
    """
    
    if number == 0:
        return 1
    
    count = 0
    while number != 0:
        number = number // 10
        count += 1
    return count