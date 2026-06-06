import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_3():
  result = main.grade("Congratulations! Today is your day. You're off to Great Places! You're off and away!")
  expected_value = "Grade 3"
  assert expected_value == result
