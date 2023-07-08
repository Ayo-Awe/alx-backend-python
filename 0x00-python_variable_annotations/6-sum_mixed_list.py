#!/usr/bin/env python3
"""This module contains a function
that returns the sum of a list of floats and
ints
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a list of
    floats
    """
    sum = 0
    for num in mxd_lst:
        sum = sum + num

    return sum
