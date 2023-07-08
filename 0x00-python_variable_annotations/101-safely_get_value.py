#!/usr/bin/env python3

"""This module contains code
for task 100
"""
from typing import Any, Union, TypeVar, Mapping

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """safely get a value"""
    if key in dct:
        return dct[key]
    else:
        return default
