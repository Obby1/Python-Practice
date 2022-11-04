def freq_counter(coll):
    """Returns frequency counter mapping of coll."""

    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    return freq_counter(str(num1)) == freq_counter(str(num2))


    # counts1 = {}
    # counts2 = {}
    # for x in num1:
    #     counts1[x] = counts1.get(x, 0) + 1

    # for x in num2:
    #     counts2[x] = counts2.get(x, 0) + 1    
    
    # return counts1 == counts2