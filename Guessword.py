import random
my_words = ('questionnaire','unconscious', 'precocious', 'liaison', 'surveillance', 'malfeasance','irascible', 'idiosyncrasy', 'foudroyant', 'eudemonic')
score = 0

def shuffler(word):
  letters=list(word)
  random.shuffle(letters)
  return ''.join(letters)



print('Guess the word'.center(120,'-'))
user_name = input('Enter your name: ')
print('Enter s to stop the game.')
for i in my_words:
  j = shuffler(i).upper()
  print('Jumbled word: ',j)
  player_input= input('Enter the guessed word: ')
  if player_input == 's':
    break
  elif  player_input == i:
    print('COORRECT')
    score+=1
  else:
    print('WRONG, The guessed word is: ',i)
print('Game over',user_name,'Your Score is: ',score)