import sys
sys.path.append("./")
sys.path.append("./../")
import cash as cash

def test_1():
  result = cash.calculate_pennies(99)
  expected_value = 99
  assert expected_value == result

def test_2():
  result = cash.calculate_pennies(1)
  expected_value = 1
  assert expected_value == result
  
def test_3():
  result = cash.calculate_pennies(0)
  expected_value = 0
  assert expected_value == result
