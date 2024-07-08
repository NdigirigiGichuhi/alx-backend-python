#!/usr/bin/env python3
"""Multiplies a float"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier that takes a float
    multiplier as argument and returns a function
    that multiplies a float by multiplier.
    """
    def multiplier_func(value: float) -> float:
        """Multiplier function"""
        return value * multiplier
    return multiplier_func
