import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_8():
  result = main.grade("There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.")
  expected_value = "Grade 9"
  assert expected_value == result
