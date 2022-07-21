import cv2
print("Loading model - be patient...\n")
print("\n...\n")
from keras.models import load_model
import numpy as np
import random
import time 

class rock_paper_scissors:
    def __init__(self, rps_list, num_lives, pcnum_lives):
        self.num_lives=num_lives
        self.rps_list=rps_list
        self.rps_list=['Rock', 'Paper', 'Scissors']
        self.pcnum_lives=pcnum_lives
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        print("\nStill loading model...\n")
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.start=time.time()
        self.end=time.time()
        self.time_elapsed=(round(self.end-self.start,1))
        self.font = cv2.FONT_HERSHEY_TRIPLEX


    def countdown(self):
        self.start=time.time()
        while True:
            self.camera_emp()
            self.end=time.time()
            cv2.putText(self.frame, '1', (10, 100), self.font, 3, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow('Rock, Paper, Scissors', self.frame)
            cv2.waitKey(1)
            self.time_elapsed=(round(self.end-self.start,1))
            if self.time_elapsed == 1:
                print(f'{self.time_elapsed}s')
                break
        while True:
            self.camera_emp()
            self.end=time.time()
            cv2.putText(self.frame, '2', (10, 100), self.font, 3, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow('Rock, Paper, Scissors', self.frame)
            cv2.waitKey(1)
            self.time_elapsed=(round(self.end-self.start,1))
            if self.time_elapsed == 2:
                self.end=time.time()
                print(f'{self.time_elapsed}s')
                break
        while True:
            self.camera_emp()
            self.end=time.time()
            cv2.putText(self.frame, '3', (10, 100), self.font, 3, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow('Rock, Paper, Scissors', self.frame)
            cv2.waitKey(1)
            self.time_elapsed=(round(self.end-self.start,1))
            if self.time_elapsed == 3:
                print(f'{self.time_elapsed}s')
                return self.time_elapsed
        
                
            
        
    def camera(self):
        ret, self.frame = self.cap.read()
        resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        cv2.putText(self.frame, 'Hold s to start game', (10, 100), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(self.frame, 'Hold q to stop game', (10, 200), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('Rock, Paper, Scissors', self.frame)
            
    def camera_go(self):
        ret, self.frame = self.cap.read()
        resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        cv2.putText(self.frame, 'Go', (10, 100), self.font, 2, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('Rock, Paper, Scissors', self.frame)
        cv2.waitKey(1500)

    def camera_emp(self):
        ret, self.frame = self.cap.read()
        resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        cv2.imshow('Rock, Paper, Scissors', self.frame)
    
    def start_game(self):
        self.camera_go()
        user_choice = self.get_prediction()
        computer_choice = self.get_computer_choice()
        self.get_winner(computer_choice,user_choice)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()
        if self.pcnum_lives == 3: 
            print('Computer wins the game!')
        if self.num_lives == 3: 
            print('User wins the game!')

    def get_prediction(self):   
        self.prediction = self.model.predict(self.data)
        idx = np.argmax(self.prediction[0])
        if idx == 0:
            idx = 'Rock'
        elif idx == 1:
            idx = 'Paper'
        elif idx == 2:
            idx = 'Scissors'
        else:
            idx = 'Nothing'
        return idx

    def get_computer_choice(self):
        computer_choice = random.choice(rps_list)
        return computer_choice
    
    def get_winner(self, computer_choice, user_prediction):
        print(f"User choice: {user_prediction}\nComputer choice: {computer_choice}")
        if user_prediction == computer_choice:
            print("The same so play again ")
            print("\nHold s to play next round of the game")
            print("Hold q to quit the game")
            return
        if user_prediction == 'Nothing':
            print("\nPlease try again - camera could not recognise\n")
            print("\nHold s to play next round of the game")
            print("Hold q to quit the game")
            return
        elif user_prediction == "Rock" and computer_choice == "Paper":
            print("Computer wins this round")
            print("\nHold s to play next round of the game")
            print("Hold q to quit the game")
            self.pcnum_lives = self.pcnum_lives +1

        elif user_prediction == "Paper" and computer_choice == "Scissors":
            print("Computer wins this round")
            print("\nHold s to play next round of the game")
            print("Hold q to quit the game")
            self.pcnum_lives = self.pcnum_lives +1

        elif user_prediction == "Scissors" and computer_choice == "Rock":
            print("Computer wins this round")
            print("\nHold s to play next round of the game")
            print("Hold q to quit the game")
            self.pcnum_lives = self.pcnum_lives +1

        else:
            print("\nUser wins this round")
            print("\nHold s to play next round of the game")
            print("Hold q to quit the game")
            self.num_lives = self.num_lives +1
        return user_prediction

    def start_camera(self):
        print("\n\nModel loaded")
        while self.num_lives < 3 and self.pcnum_lives < 3: 
            self.camera()
            if cv2.waitKey(10) & 0xFF == ord('s'):
                self.countdown()
                if self.time_elapsed == 3:
                    self.camera_go()
                    self.start_game()
                    print(f'Total computer wins {self.pcnum_lives} and Total user wins {self.num_lives}\n\n')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.cap.release()
                cv2.destroyAllWindows()
                break                
            


def play(rps_list):
    game = rock_paper_scissors(rps_list, num_lives=0, pcnum_lives=0)
    game.start_camera()

if __name__ == '__main__':
    rps_list = ['Rock','Paper','Scissors']
    play(rps_list)





