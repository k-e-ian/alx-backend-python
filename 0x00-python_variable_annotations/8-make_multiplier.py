#!/usr/bin/env python3
'''
file 8-make_multiplier.py
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(x: float) -> float:
        '''
        Takes float value(multiplier) returns product of x and multiplier
        '''
        return x * multiplier
    return multiply
