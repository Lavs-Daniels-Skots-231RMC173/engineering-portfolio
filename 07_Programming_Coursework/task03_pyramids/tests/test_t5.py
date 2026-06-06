import unittest
import sys
sys.path.append("./")
sys.path.append("./../")
import t5

def test_f5_01():
    assert t5.draw(5) == "1********1\n12******21\n123****321\n1234**4321\n1234554321\n"