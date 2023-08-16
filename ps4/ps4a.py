# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
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
    if (len(sequence) == 1):
        return [sequence]
    else:
        permutations = []  # empty list to store return

        # enumerate function to eliminate nested for loop
        for i, letter in enumerate(sequence):
            permutations += [letter +
                             p for p in get_permutations(sequence[:i]+sequence[i+1:])]  # for each letter, feed the remaining chars into recursive function.
        # used set so stuff like 'abb' would not return multiple of the same combo.
        return list(set(permutations))


if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    def test_answer():
        x = time.process_time
        # Example test case 1
        example_input = 'abc'
        print("\nBASIC INPUT TEST")
        print(f"Input: {example_input}")
        print("Expected Output:, ['bac', 'bca', 'abc', 'cba', 'cab', 'acb']")
        print(f"Actual Output:' {get_permutations(example_input)} \n")

        # Example test case 2
        example_input = 'abb'
        print("SET TEST")
        print(f"Input: {example_input}")
        print("Expected Output: ['bab', 'abb', 'bba']")
        print(f"Actual Output: {get_permutations(example_input)} \n")

        # Example test case 3
        example_input = 'daniel'
        print("LENGTH TEST")
        print(f"Input: {example_input}")
        print("Len should be 720")
        print(f"Len is actually {len(get_permutations(example_input))} \n")

        print(get_permutations('abbbbbbbbb'))

    test_answer()
