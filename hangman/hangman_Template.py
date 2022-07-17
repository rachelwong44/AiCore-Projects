'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
from os import replace
import random
from tkinter import E, N, WORD

class Hangman:

    hangmanpictures=['''
__________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                                                 
    |__
    ''',
    '''
___________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                                            
    |__
    ''',
    '''
___________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                                                     
    |__
    ''',
    '''
__________                  
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                                                           
    |__
    ''',
    '''
__________
    |    |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \                  
    |__
YOU HAVE LOST THE GAME!
'''
]

    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
'''
    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        self.word_list=word_list
        self.word=random.choice(word_list)
        self.word_guessed=[]
        self.num_letters=int
        self.num_lives= num_lives
        self.list_letters=[]
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
        
        print(f"The mystery word has {len(self.word)} characters")
        for i in range(len(self.word)):
            self.word_guessed.append("_")
        print(f"{self.word_guessed}", end="")

        pass

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase    
        if letter.lower() in self.word:
            print("\nLetter in the word")
            self.list_letters.append(self.letter)

            # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
            # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
            
            indices=[]
            print(self.word)
            for index, value in enumerate(self.word):
                if value == self.letter:
                    indices.append(index)
            
            for i in indices:
                self.num_letters=0
                self.word_guessed[i]=self.letter
                self.num_letters += 1

            print(self.num_letters)
            print(f"The mystery word has {self.num_letters} characters left to guess!")
            print(f"{self.word_guessed}", end="")
            Hangman.ask_letter(self)

        elif letter.lower() not in self.word:
                print("\nLetter not in the word")     

            # TODO 3: If the letter is not in the word, reduce the number of lives by 1
                self.num_lives= self.num_lives - 1
                print(f"You have {self.num_lives} lives left")
                print(Hangman.hangmanpictures[-self.num_lives-1])
                Hangman.ask_letter(self)
        else:
            return 
    
        # Be careful! A word can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        
        while self.num_lives>0:  # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter - 
            #Loop runs without any conditions until break statement executes inside the loop - #
            self.letter= str(input('\nGuess a letter: \n')) # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
            if len(self.letter) !=1:
                print("Please, enter just one character")
            elif self.letter.lower() not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a letter not a special or numerical character')
            elif self.letter.lower() in self.list_letters:
                self.list_letters.append(self.letter)
                print(f"{self.letter} was already tried")
            else:              
                Hangman.check_letter(self,self.letter)
                return 
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method.
        pass



def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    # TODO 1: To test this task, you can call the ask_letter method
    game.ask_letter()
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    

    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"
    while True:
        if game.num_lives == 0:
            print(f"You ran out of lives. The word was {game.word}\n")
        # If the user guesses the word, print "Congratulations, you won!"
        elif "_" not in [i for i in game.word_guessed]:
            print("Congratulations you have won!")

    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
