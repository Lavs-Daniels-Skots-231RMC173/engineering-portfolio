import sys
sys.path.append("./")
sys.path.append("./../")
import cash as cash

def test_1():
  result = cash.coin_count(99)
  expected_value = 9
  assert expected_value == result

def test_2():
  result = cash.coin_count(26)
  expected_value = 2
  assert expected_value == result
  
def test_3():
  result = cash.coin_count(25)
  expected_value = 1
  assert expected_value == result
    
def test_4():
  result = cash.coin_count(24)
  expected_value = 6
  assert expected_value == result
    
def test_5():
  result = cash.coin_count(5)
  expected_value = 1
  assert expected_value == result

def test_6():
  result = cash.coin_count(4)
  expected_value = 4
  assert expected_value == result
  
def test_7():
  result = cash.coin_count(1)
  expected_value = 1
  assert expected_value == result

def test_8():
  result = cash.coin_count(0)
  expected_value = 0
  assert expected_value == result
