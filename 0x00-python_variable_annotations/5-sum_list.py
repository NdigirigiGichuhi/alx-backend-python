#!/usr/bin/env python3
"""Sum of a list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    sum = 0
    for f in input_list:
        sum += f

    return sum
