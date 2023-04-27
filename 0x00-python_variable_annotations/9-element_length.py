#!/usr/bin/env python3
'''
file 9-element_length.py
'''
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    returns values with the appropriate type
    '''
    return [(i, len(i)) for i in lst]
