import pytest
from mypkg.my_answers import build_tree


def test_example1():
    list = [9, 7, 12, None, None, 3, None]
    a = build_tree(None, list, 0)

    assert (a.data == 9)
    assert (a.left.data==7)
    assert (a.left.left is None)
    assert (a.left.right is None)

    assert (a.right.data == 12)
    assert (a.right.left.data == 3)
    assert (a.right.right is None)


def test_example2():
    list2 = [1, 3, None]
    b = build_tree(None, list2, 0)

    assert (b.data == 1)
    assert (b.left.data == 3)
    assert (b.right is None)


def test_example3():
    list3 = [9, 7, 12, 1, 2, 3, None, 0, 0]
    c = build_tree(None, list3, 0)

    assert (c.data == 9)
    assert (c.left.data == 7)
    assert (c.left.left.data == 1)
    assert (c.left.right.data == 2)

    assert (c.left.left.left.data == 0)
    assert (c.left.left.right.data == 0)

    assert (c.right.data == 12)
    assert (c.right.left.data == 3)
    assert (c.right.right is None)