import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_1():
  result = main.grade("One fish. Two fish. Red fish. Blue fish.")
  expected_value = "Before Grade 1"
  assert expected_value == result
