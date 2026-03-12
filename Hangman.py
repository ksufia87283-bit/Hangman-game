import random
print('Welcome to the Hangman game!!')
print('Guess the animal name!')
animals=['zebra','cat','parrot','giraffe','monkey','dog','bunny','cheeta','Tiger','eagle']
word=random.choice(animals) 
guessed_letter=set()
hangman_stages=[
    """
       ------
       |    |
       |    
       |    
       |    
       |    
    --------""",
 """
       ------
       |    |
       |    o
       |    
       |    
       |    
    --------""",
     """
       ------
       |    |
       |    o
       |    |
       |    
       |    
    --------""",
    """
       ------
       |    |
       |    o
       |   /|
       |    
       |    
    --------""",
    """
       ------
       |    |
       |    o
       |   /|\\
       |    
       |    
    --------""",
       """
       ------
       |    |
       |    o
       |   /|\\
       |   /
       |    
    --------""",
       """
       ------
       |    |
       |    o
       |   /|\\
       |   / \\
       |    
    --------""",]

displayed_word = ''.join([letter if letter in guessed_letter else "_" for letter in word]) 
print(displayed_word)
attempt=6
while attempt>=1:
    print(hangman_stages[6-attempt])
    userletter=str(input('Guess a letter: '))
    if len(userletter)!=1 or not userletter.isalpha():
        print('Error, please enter a valid letter!⚠️')
        continue
    if userletter in guessed_letter:
        print('OoOpS, You already guessed the letter.👎')
        continue
    guessed_letter.add(userletter)
    if userletter in word:
        print('Good guess!😀')
    else:
        print('Womp womp womp😩')
        print('Lost an attempt..❌')
        attempt=attempt-1
    displayed_word = ''.join([letter if letter in guessed_letter else "_" for letter in word]) 
    print(displayed_word)
    print('You have', attempt,'attempts left!' )
    if set(word).issubset(guessed_letter):
        print('You have won the game, CongratS!!🎊🎉')
        break
if attempt==0:
    print(hangman_stages[-1])
    print('You have lost, womp womp womp')
    print('The word was', word)
    print('Better luck next time')

#hangman figure

        #   o
        #  /|\
        #  /\
           
# Printing statement for interaction
# List of animals
# Choose Random animal name for guessing from list
# Store already_guessed letter in a set
# Create a hangman stages
# Write underscores _ 
# displayed_word = ''.join([letter if letter in guessed_letter else "_" for letter in word])
# Print underscores thing
# Start a while loop
# Print hangman stages
# Ask from the user to guess a letter
# Create error messages
# Create error for already attempt for already guessed letter
# whatever user guess, store everything in the guessed_letter
# Create a if condition right, write a good guess
#  if condition is wrong, write wrong guess
# Update underscores thing
# Show the attempts left
# If user guessed full word, then write congratulations
# Outside of the loop, if the attempt becomes 0, user lost the game



