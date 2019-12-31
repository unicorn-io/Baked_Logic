import re
import itertools

def solve(puzzle):
    '''Solves the cryptarithm puzzle by permuting over all cases

    Parameters:
    arg* string: the puzzle

    Return:
    string: the evaluated puzzle
    '''
    words = re.findall("[A-Z]+", puzzle)
    unique_chars = set(''.join(words))
    assert(len(unique_chars)) <= 10, "Bad Input Call: Chars more than 10"
    first_letters = {word[0] for word in words}
    sorted_chars = ''.join(first_letters) + \
        ''.join(unique_chars - first_letters)
    chars = tuple(ord(c) for c in sorted_chars)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(chars)):
        if zero not in guess[:len(first_letters)]:
            equation = puzzle.translate(dict(zip(chars, guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)
        else:
            print("Bad Call: No Solution For this puzzle")