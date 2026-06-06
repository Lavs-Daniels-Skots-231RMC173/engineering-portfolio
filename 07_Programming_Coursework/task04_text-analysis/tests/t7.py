import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_7():
  result = main.grade("When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.")
  expected_value = "Grade 8"
  assert expected_value == result
