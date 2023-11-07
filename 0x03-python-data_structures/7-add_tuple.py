#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None:
        tuple_a = ()
    if tuple_b is None:
        tuple_b = ()
    if len(tuple_a) > 0:
        fst_fst = tuple_a[0]
    else:
        fst_fst = 0
    if len(tuple_a) > 1:
        fst_scd = tuple_a[1]
    else:
        fst_scd = 0
    if len(tuple_b) > 0:
        scd_fst = tuple_b[0]
    else:
        scd_fst = 0
    if len(tuple_b) > 1:
        scd_scd = tuple_b[1]
    else:
        scd_scd = 0
    return fst_fst + scd_fst, fst_scd + scd_scd
