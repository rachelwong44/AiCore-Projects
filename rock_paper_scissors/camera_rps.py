import cv2
from keras.models import load_model
import numpy as np
import random
import time 

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class rock_paper_scissors:

    def __init__(self, rps_list, num_lives=0, pcnum_lives=0):
        self.model = load_model('keras_model.h5')
        self.num_lives=num_lives
        self.rps_list=rps_list
        self.rps_list=['Rock', 'Paper', 'Scissors']
        self.pcnum_lives=pcnum_lives

        def countdown(self, count): 
            seconds=3
            start=time.time()
            while seconds >0:
                end=time.time()
                if start >= end:
                    seconds= seconds -1
                    final_time = end
                    return final_time



        def get_prediction(self):         #return output of model with probabilities = confidence - pick highest probability
            predictions = self.model.predict(self.data)
            idx = np.argmax(predictions[0])
            return idx

        def get_computer_choice(self):
            computer_choice = random.choice(rps_list)
            return computer_choice
        
        def get_winner(self, computer_choice, user_prediction):
            print(f"User choice: {user_prediction}\nComputer choice: {computer_choice}")
            if user_prediction == computer_choice:
                print("The same so play again ")

            elif user_prediction == "Rock" and computer_choice == "Paper":
                print("Computer wins this round")
                self.pcnum_lives = self.pcnum_lives +1

            elif user_prediction == "Paper" and computer_choice == "Scissors":
                print("Computer wins this round")
                self.pcnum_lives = self.pcnum_lives +1

            elif user_prediction == "Scissors" and computer_choice == "Rock":
                print("Computer wins this round")
                self.pcnum_lives = self.pcnum_lives +1

            else:
                print("User wins this round")
                self.num_lives = self.num_lives +1
            return 

def play(rps_list):
    game = rock_paper_scissors(rps_list, num_lives=0)
    while game.num_lives<= 3 and game.pcnum_lives<= 3:
        a=game.get_computer_choice()
        print("Please input from keyboard R=Rock, P=Paper, S=Scissors")
        b=game.get_prediction()
        game.get_winner(a, b)
        print(f'\nTotal computer wins {game.pcnum_lives} and Total user wins {game.num_lives}')
        if game.pcnum_lives == 3: 
            print('\nComputer wins the game!')
            break
        if game.num_lives == 3: 
            print('\nUser wins the game!')
            break

if __name__ == '__main__':
    rps_list = ['Rock','Paper','Scissors']
    play(rps_list)


