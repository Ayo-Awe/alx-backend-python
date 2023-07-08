#!/usr/bin/env python3

"""This module contains a function
element_length
"""
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing an element and it's
    lengths"""
    return [(i, len(i)) for i in lst]
