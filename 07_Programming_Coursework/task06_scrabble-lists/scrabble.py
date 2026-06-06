# this list has as many values as there are letters in alphabet : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def get_string(a):
  # request input
  text = input("Player " + str(a)+": ")
  return text


# TODO: this function should have an argument
def compute_score(word):
  score = 0
  # in a loop
  # transform to lower
  word = word.lower()
  for char in word:
  # check if alnumerics
    if char.isalpha():
  # if alnumeric, get the ord number of letter, substract a value and get an index for POINTS
      score += POINTS[ord(char)-97]
  return score

def main():
  # TODO: finish all functions
  word1 = get_string(1)
  word2 = get_string(2)

  # get points
  points1 = compute_score(word1)
  points2 = compute_score(word2)
  # compare who wins
  # write IF here
  if points1 > points2:
    print ("Player 1 wins!")
  elif points1 < points2:
    print ("Player 2 wins!")
  else:
    print ("Tie!")
if __name__ == "__main__":
  main()