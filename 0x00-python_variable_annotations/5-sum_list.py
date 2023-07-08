#!/usr/bin/env python3
"""This module contains a function
that returns the sum of a list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of a list of
    floats
    """
    sum = 0
    for num in input_list:
        sum = sum + num

    return sum
