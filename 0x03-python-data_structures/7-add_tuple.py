#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a
    tuple_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b
    new_tpl = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tpl
