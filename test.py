import pytest
from dictionary_tree import DictTreeNode, DictionaryTree


def test_add_word():
    tree = DictionaryTree()
    tree.add_word("lol")
    print(repr(tree.dictionary))
