#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or len(sentence) == 0:
        a = 0
        b = None
    else:
        a = len(sentence)
        b = sentence[0]
    return a, b
