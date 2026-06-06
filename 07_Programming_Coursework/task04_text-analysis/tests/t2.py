import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_2():
  result = main.grade("Would you like them here or there? I would not like them here or there. I would not like them anywhere.")
  expected_value = "Grade 2"
  assert expected_value == result
