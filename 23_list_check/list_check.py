def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # for items in lst:
    #     if isinstance(items, list) == False:
    #         return False
    # return True

# SB solution. if NOT true, return false
# 
    for item in lst:
        # if item is not an instance of list
        if not isinstance(item, list):
            return False

    return True    