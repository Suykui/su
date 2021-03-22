import pytest
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from coding import tree

def test_one():
    assert tree.bianry_tree(before='abc',mid='bac') == 'bca'
    assert tree.bianry_tree(behind='bca',mid='bac') == 'abc'

if __name__ == '__main__':
    pytest.main('test_tree.py')