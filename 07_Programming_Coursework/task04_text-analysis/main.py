def letter_count(text):
  # TODO: add passed variable for this function, use it in calculations
  count = 0
  for char in text:
    if char.isalpha():
      count += 1
  return count

def word_count(text):
  # TODO: add passed variable for this function, use it in calculations
  count = 0
  for word in text.split():
    count += 1
  return count

def punctuation_count(text):
  # TODO: add passed variable for this function, use it in calculations
  count = 0
  for char in text:
    if char == "." or char == "!" or char == "?":
      count +=1
  return count

def grade(text):
  # TODO: add passed variable for this function, use it in calculations. 
  # Call letter_count, word_count and punctuation_count functions from this function.
  letters = letter_count(text)
  print(letters)
  words = word_count(text)
  print(words)
  punctuation = punctuation_count(text)
  print(punctuation)
  L = (letters / words) * 100 
  S = (punctuation / words) * 100 
  index = 0.0588 * L - 0.296 * S - 15.8
  if index < 1:
    return "Before Grade 1"
  elif index > 16:
    return "Grade 16+"
  else:
    return f"Grade {round(index)}"  
  
def main():
  # TODO: input, call grading function and the print return from grading.
  text = input("Text: ")
  print(grade(text))


# this calls the main function if this is the file where you press run/play button
if __name__ == "__main__":
  main()

