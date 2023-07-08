#!/usr/bin/env python3

"""This module contains a function
that rereturns a tuple with k as the
first argument and the square of v
as the second argument
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple with k as the
    first argument and the square of v
    as the second argument
    """

    return (k, v**2)
