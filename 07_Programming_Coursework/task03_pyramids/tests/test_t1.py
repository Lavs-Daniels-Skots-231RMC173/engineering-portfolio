import unittest
import sys
sys.path.append("./")
sys.path.append("./../")
import t1

def test_f1_01():
    assert t1.draw(3) == "1\n12\n123\n"

def test_f1_02():
    assert t1.draw(5) == "1\n12\n123\n1234\n12345\n"
