import unittest
import sys
sys.path.append("./")
sys.path.append("./../")
import t3

def test_f3_01():
    assert t3.draw(2) == " #  # \n##  ##\n"

def test_f3_02():
    assert t3.draw(4) == "   #  #   \n  ##  ##  \n ###  ### \n####  ####\n"
