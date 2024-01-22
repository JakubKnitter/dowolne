import pytest

def dodawanie(a,b):
    return a + b

assert dodawanie(5, 3) == 8
assert dodawanie(-1, 1) == 0
assert dodawanie(0, 3) == 3