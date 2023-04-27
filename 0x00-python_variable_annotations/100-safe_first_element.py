#!/usr/bin/env python3
'''
file 100-safe_first_element.py
'''
from typing import Sequence, Any, Union, Optional, List


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    '''
    returns values with the appropriate type not known input
    '''
    if lst:
        return last[0]
    else:
        return None
