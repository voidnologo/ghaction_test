from x import add


def test_add_ints():
    assert add(1, 2) == 3


def test_add_strs():
    assert add('a', 'b') == 'ab'


def test_add_lists():
    assert add(['a'], ['b']) == ['a', 'b']
