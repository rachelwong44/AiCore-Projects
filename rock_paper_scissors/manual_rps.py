import random

class rock_paper_scissors:
    def __init__(self, rps_list, num_lives=0, pcnum_lives=0):
        self.num_lives=num_lives
        self.rps_list=rps_list
        self.rps_list=['Rock', 'Paper', 'Scissors']
        self.pcnum_lives=pcnum_lives

        
    def get_computer_choice(self):
        computer_choice = random.choice(rps_list)
        return computer_choice

    def get_winner(self, computer_choice, user_choice):
        print(f"User choice: {user_choice}\nComputer choice: {computer_choice}")
        if user_choice == computer_choice:
            print("The same so play again ")

        elif user_choice == "Rock" and computer_choice == "Paper":
            print("Computer wins this round")
            self.pcnum_lives = self.pcnum_lives +1

        elif user_choice == "Paper" and computer_choice == "Scissors":
            print("Computer wins this round")
            self.pcnum_lives = self.pcnum_lives +1

        elif user_choice == "Scissors" and computer_choice == "Rock":
            print("Computer wins this round")
            self.pcnum_lives = self.pcnum_lives +1

        else:
            print("User wins this round")
            self.num_lives = self.num_lives +1
        return 


    def get_user_choice(self):
        letter= str(input('\nInput User choice: ')).upper()
        out = ""
        if letter == "R":
            out = "Rock"
        elif letter =="P":
            out = "Paper"
        elif letter == "S":
            out = "Scissors"
        else:
            print("Please input either R, P, or S")
            self.get_user_choice()
        #print(f"User choice: {out}")
        return out 

def play(rps_list):
    game = rock_paper_scissors(rps_list, num_lives=0)
    while game.num_lives<= 3 and game.pcnum_lives<= 3:
        a=game.get_computer_choice()
        print("Please input from keyboard R=Rock, P=Paper, S=Scissors")
        b=game.get_user_choice()
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


  
