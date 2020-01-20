from x import add
from x import multiply


def test_add_ints():
    assert add(1, 2) == 3


def test_add_strs():
    assert add('a', 'b') == 'ab'


def test_add_lists():
    assert add(['a'], ['b']) == ['a', 'b']


def test_multiply_ints():
    assert multiply(1, 2) == 2


def test_multiply_str():
    assert multiply('a', 3) == 'aaa'


def test_multiply_list():
    assert multiply(['a'], 3) == ['a', 'a', '']


def test_passes():
    assert True
