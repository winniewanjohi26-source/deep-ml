def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    n = len(samples)
    count = {}
    for num in samples:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    #print(count)
    probability = []
    for num, freq in count.items():
        prob = freq/n
        probability.append((num,prob))
    return probability

    pass