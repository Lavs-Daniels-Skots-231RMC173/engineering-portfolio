import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_9():
  result = main.grade("It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.")
  expected_value = "Grade 10"
  assert expected_value == result
