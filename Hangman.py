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




