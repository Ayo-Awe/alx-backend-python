#!/usr/bin/env python3

"""This module contains a function
that creates a multiplier function
"""
from typing import Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a multiplier function
    """
    return lambda x: multiplier * x
