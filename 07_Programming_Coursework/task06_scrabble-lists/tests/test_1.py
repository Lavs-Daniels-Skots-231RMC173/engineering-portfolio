import sys
sys.path.append("./")
sys.path.append("./../")
import scrabble

def test_01():
  result = scrabble.compute_score("Scrabble")
  expected_value = 14
  assert expected_value == result
  
def test_02():
  result = scrabble.compute_score("wiNNer")
  expected_value = 9
  assert expected_value == result

def test_03():
  result = scrabble.compute_score("Question?")
  expected_value = 17
  assert expected_value == result

def test_04():
  result = scrabble.compute_score("Question!")
  expected_value = 17
  assert expected_value == result

def test_05():
  result = scrabble.compute_score("Oh,")
  expected_value = 5
  assert expected_value == result

def test_06():
  result = scrabble.compute_score("hai!")
  expected_value = 6
  assert expected_value == result

def test_07():
  result = scrabble.compute_score("COMPUTER")
  expected_value = 14
  assert expected_value == result

def test_08():
  result = scrabble.compute_score("science")
  expected_value = 11
  assert expected_value == result

def test_09():
  result = scrabble.compute_score("123")
  expected_value = 0
  assert expected_value == result

def test_10():
  result = scrabble.compute_score("game")
  expected_value = 7
  assert expected_value == result
