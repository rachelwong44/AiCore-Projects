import cv2
print("Loading model - be patient...\n")
print("\n...\n")
#from keras.models import load_model
import numpy as np
import random
import time 

class rock_paper_scissors:
    def __init__(self, rps_list, num_lives, pcnum_lives):
        self.num_lives=num_lives
        self.rps_list=rps_list
        self.rps_list=['Rock', 'Paper', 'Scissors']
        self.pcnum_lives=pcnum_lives
        self.start=time.time()
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        print("\nStill loading model...\n")
        #self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)

    def countdown(self): 
        while True:
            end=time.time()
            time_elapsed=(round(end-self.start,1))
            if time_elapsed == 1:
                print(f'{time_elapsed}s')
                break
        while True:
            end=time.time()
            time_elapsed=(round(end-self.start,1))
            if time_elapsed == 2:
                end=time.time()
                print(f'{time_elapsed}s')
                break
        while True:
            end=time.time()
            time_elapsed=(round(end-self.start,1))
            if time_elapsed == 3:
                print(f'{time_elapsed}s')
                break 

    def camera(self):
        ret, self.frame = cap.read()
        resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        cv2.imshow('frame', self.frame)

    def get_prediction(self):         #return output of model with probabilities = confidence - pick highest probability
        predictions = self.model.predict(self.data)
        idx = np.argmax(predictions[0])
        return idx
        print(idx)

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
    game = rock_paper_scissors(rps_list, num_lives=0, pcnum_lives=0)
    while game.num_lives<= 3 and game.pcnum_lives<= 3:
        #game.camera()
        #cap.release()
        #cv2.destroyAllWindows()
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break
        print("Show your hand after a count to 3:")
        game.countdown()
        a=game.get_computer_choice()
        b=game.get_prediction()
        game.get_winner(a, b)
        print(f'\nTotal computer wins {game.pcnum_lives} and Total user wins {game.num_lives}')
        if game.pcnum_lives == 3: 
            print('\nComputer wins the game!')
            break
        if game.num_lives == 3: 
            print('\nUser wins the game!')
            break
        print('Press q to close the window')


if __name__ == '__main__':
    rps_list = ['Rock','Paper','Scissors']
    play(rps_list)



