#!/usr/bin/env python3
'''
file 7-to_kv.py
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Takes a string k and an int or float v as args and returns a tuple.
    returns tuple(string k, int/float v) and should be annotated as a float.
    '''
    return (k, float(v**2.0))
