import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_0_3():
  result = main.word_count("Congratulations! Today is your day. You're off to Great Places! You're off and away!")
  expected_value = 14
  assert expected_value == result
