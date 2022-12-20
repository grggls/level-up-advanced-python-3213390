def pairwise_offset(sequence, fillvalue='*', offset=0):
    # add 'offset' number of 'fillvalue' to the end of 'sequence'
    # so pairwise_offset('abcde', '*', 2) creates 'abcde**'
    sequence += fillvalue * offset
    pairwise = []

    for cursor in range(0, len(sequence)):
        pairwise.append((sequence[cursor], sequence[cursor-offset]))

    return pairwise
