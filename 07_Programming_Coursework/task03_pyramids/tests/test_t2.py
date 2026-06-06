import unittest
import sys
sys.path.append("./")
sys.path.append("./../")
import t2

def test_f2_01():
    assert t2.draw(5) == "2\n24\n"

def test_f2_02():
    assert t2.draw(11) == "2\n24\n246\n2468\n246810\n"
