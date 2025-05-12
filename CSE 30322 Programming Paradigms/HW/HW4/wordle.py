import random

class Guess:
  good_letters = set()
  bad_letters = set()
  correct_letters = ['']*5

  # creates a guess object with word, letter list, and set of outputs that need to be displayed.
  def __init__(self, word):
    self.word = word
    self.letters_list = list(word)
    self.letters = set(self.letters_list) 
    self.get_good_letters()
    self.get_bad_letters()
    self.solved_count = 0
    self.solved = False
    self.get_correct_letters()

  # returns an intersection of the set of guess letters and answer letters
  def get_good_letters(self):
    Guess.good_letters = Guess.good_letters | self.letters.intersection(Guess.answer_set)
  
  # returns a difference of the set of guess letters and answer letters.
  def get_bad_letters(self):
    Guess.bad_letters = Guess.bad_letters | self.letters.difference(Guess.answer_set)
  
  # returns a list of letters in guess that are correct (right letter and right location).
  def get_correct_letters(self):
    for i in range(5):
      if self.letters_list[i] == Guess.answer_list[i]:
        Guess.correct_letters[i] = self.letters_list[i]
        self.solved_count+=1
    if self.solved_count == 5:
      self.solved = True

  # method that sets static variables for the whole class.
  def set_answer_static(answer_word):
    Guess.answer = answer_word
    Guess.answer_list = list(answer_word)
    Guess.answer_set = set(Guess.answer_list)

# read in words.txt into list and making sure they are uppercase.
words = []
with open('words.txt', 'r') as file:
  for line in file:
    words.append(line.strip().upper()) 

# choosing a word from the list to set as answer.
Guess.set_answer_static(words[random.randint(0, len(words)-1)])

# writing the answer to answer.txt.
with open('answer.txt', 'w') as file:
  file.write(Guess.answer)

# loop through 6 guesses.
for i in range(1,7):
  # Ask for a guess until a proper guess is given
  guess_word = input(f"Turn {i}. Guess a word: ").upper()
  while len(guess_word) != 5 or guess_word not in words:
    print(f'{guess_word} is not a valid guess')
    guess_word = input(f"Turn {i}. Guess a word: ").upper()

  # initializes the Guess object.
  guess = Guess(guess_word)

  # checks if solved and breaks then.
  if guess.solved:
    break

  # if not it prints info and tells the user to guess again.
  print("Good Letters: " + str(list(Guess.good_letters)) + '\n' "Bad Letters: " + str(list(Guess.bad_letters)) + '\n' + "Correct Letters: " +  str(Guess.correct_letters))
  print('Try Again')

# prints the correct output according to the what has happened.
if guess.solved:
  print(f'Congratulations, you correctly identified the word after {i} attempt(s)')
else:
  print(f'The answer is {Guess.answer}. You did not correctly guess it within 6 tries.')
  