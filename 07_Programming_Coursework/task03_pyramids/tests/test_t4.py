import unittest
import sys
sys.path.append("./")
sys.path.append("./../")
import t4

def test_f4_01():
    assert t4.draw(3) == "**3\n*23\n123\n"

def test_f4_02():
    assert t4.draw(5) == "****5\n***45\n**345\n*2345\n12345\n"
