import pytest
from mypkg.my_answers import BinaryTree


def test_example1():
    my_tree = BinaryTree(5)
    my_tree.add_left(4)
    my_tree.add_right(3)

    assert (my_tree.node == 5)
    assert (my_tree.left.node == 4)
    assert (my_tree.right.node == 3)


def test_example2():
    a = BinaryTree(1)
    b = BinaryTree(2, 0.1, 0.2)
    c = BinaryTree(3)
    a.left = b
    a.right = c

    assert (a.node == 1)
    assert (a.left.node == 2)
    assert (a.left.left == 0.1)
    assert (a.left.right == 0.2)
    assert (a.right.node == 3)


def test_example3():
    a = BinaryTree(1)
    b = BinaryTree(2, 0.1, 0.2)
    c = BinaryTree(3)
    a.left = b
    a.right = c

    assert (a.is_leaf() is False)
    assert (b.is_leaf() is False)
    assert (c.is_leaf() is True)
