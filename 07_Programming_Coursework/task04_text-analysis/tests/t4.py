import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_4():
  result = main.grade("Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.")
  expected_value = "Grade 5"
  assert expected_value == result
