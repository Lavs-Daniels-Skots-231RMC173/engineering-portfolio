import sys
sys.path.append("./")
sys.path.append("./../")
import nutrition

def test_1():
  result = nutrition.find_fruit("apple")
  expected_value = 130
  assert expected_value == result

def test_2():
  result = nutrition.find_fruit("APPLE")
  expected_value = 130
  assert expected_value == result
  
def test_3():
  result = nutrition.find_fruit("sweet cherries")
  expected_value = 100
  assert expected_value == result

def test_4():
  result = nutrition.find_fruit("tangerines")
  expected_value = "try again"
  assert expected_value == result

