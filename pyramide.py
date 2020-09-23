"""Program that creates beautiful pyramids."""
from math import ceil


def get_char(base, char, row, element):
    """Help get white spaces."""
    spaces = ceil(base / 2) - row - 1
    if element in range(0, spaces) or element in range(base - spaces, base):
        return ' '
    else:
        return char


def make_pyramid(base: int, char: str) -> list:
    """
    Construct a pyramid with given base.

    Pyramid should consist of given chars, all empty spaces in the pyramid list are ' '. Pyramid height depends on base length. Lowest floor consists of base-number chars.
    Every floor has 2 chars less than the floor lower to it.
    make_pyramid(3, "A") ->
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    make_pyramid(6, 'a') ->
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    :param base: int
    :param char: str
    :return: list
    """
    height = ceil(base / 2)  # listis on nii mitu elementi
    pyramid = [[get_char(base, char, row, element) for element in range(base)] for row in range(height)]
    return pyramid


def join_pyramids(pyramid_a: list, pyramid_b: list) -> list:
    """
    Join together two pyramid lists.

    Get 2 pyramid lists as inputs. Join them together horizontally. If the the pyramid heights are not equal, add empty lines on the top until they are equal.
    join_pyramids(make_pyramid(3, "A"), make_pyramid(6, 'a')) ->
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]

    :param pyramid_a: list
    :param pyramid_b: list
    :return: list
    """
    max_height = max(len(pyramid_a), len(pyramid_b))

    if len(pyramid_a) == max_height:
        base = len(pyramid_b[0])
        for i in range(max_height - len(pyramid_b)):
            empty_line = [" " for i in range(base)]
            pyramid_b.insert(0, empty_line)
    elif len(pyramid_b) == max_height:
        base = len(pyramid_a[0])
        for i in range(max_height - len(pyramid_a)):
            empty_line = [" " for i in range(base)]
            pyramid_a.insert(0, empty_line)

    return [a + b for a, b in zip(pyramid_a, pyramid_b)]


def to_string(pyramid: list) -> str:
    """
    Return pyramid list as a single string.

    Join pyramid list together into a string and return it.
    to_string(make_pyramid(3, 'A')) ->
    '''
     A
    AAA
    '''

    :param pyramid: list
    :return: str
    """
    return "\n".join(["".join(sth) for sth in pyramid])
