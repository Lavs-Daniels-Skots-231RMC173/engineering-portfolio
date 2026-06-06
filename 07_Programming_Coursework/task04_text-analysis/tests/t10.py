import sys
sys.path.append("./")
sys.path.append("./../")
import main

def test_10():
  result = main.grade("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.")
  expected_value = "Grade 16+"
  assert expected_value == result
