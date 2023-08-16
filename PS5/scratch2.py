

import time


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # Base case
    if len(sequence) == 1:
        return [sequence]

    # Recursive cases
    else:
        # Set up list to be returned
        perms = []
        last_letter = sequence[-1]
        sequence = sequence[:-1]
        prev_perm_list = get_permutations(sequence)

        # Insert 'last_letter' at each position for each permutation
        for p in prev_perm_list:
            for pos in range(0, len(p)+1):
                new_p = p[:pos] + last_letter + p[pos:]
                perms.append(new_p)

        return list(set(perms))


start_time = time.time()
print(get_permutations("abcdefghij"))
print("--- %s seconds ---" % (time.time() - start_time))
