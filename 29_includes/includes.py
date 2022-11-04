def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    #if collection is an instance of dict, return sought in collection.values
    #dict is unordered no need to search for start
    if isinstance(collection, dict):
        return sought in collection.values()
    
    if isinstance(collection, set) or start == None:
        return sought in collection
    
    # strings, lists, can be accessed with [::] notation / slice
    return sought in collection[start::]

    #     if isinstance(collection, dict):
    #     # .values() is iterable with in
    #     return sought in collection.values()

    # if start is None or isinstance(collection, set):
    #     # [] notation will mess up in loop in set
    #     # if none or set, can't use [] after collection
    #     return sought in collection

    # return sought in collection[start:]

    
