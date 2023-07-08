#!/usr/bin/env python3

"""This module contains code
for task 100
"""
from typing import Any, Union


def safe_first_element(lst: Any) -> Union[Any, None]:
    """returns an element only if the lst is not
    null
    """

    if lst:
        return lst[0]
    else:
        return None
