#!/usr/bin/env python3
'''
file 101-safely_get_value.py
'''


from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, Any]:
    '''
    returns values with the appropriate type not known input u    sing TypeVar
    '''
    if key in dct:
        return dct[key]
    else:
        return default
