import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_0_1():
  result = main.letter_count("Congratulations! Today is your day. You're off to Great Places! You're off and away!")
  expected_value = 65
  assert expected_value == result
