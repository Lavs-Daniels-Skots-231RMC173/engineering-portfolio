import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_5():
  result = main.grade("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.")
  expected_value = "Grade 7"
  assert expected_value == result
