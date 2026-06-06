import unittest
import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_f1_01():
    assert main.choice(5, 4) == "Value 1 is bigger than Value 2"

def test_f1_02():
    assert main.choice(3, 4) == "Value 1 is smaller than Value 2"

def test_f1_03():
    assert main.choice(4, 4) == "Both values are the same"