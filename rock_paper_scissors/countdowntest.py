from __future__ import print_function
from os import times
import time
from turtle import end_poly


#def countdown(self): 

start=time.time()
start_sec=time.time()
#seconds=3
time_elapsed=[]

def countdown():
    while True:
        end=time.time()
        time_elapsed=(round(end-start,1))
        #print(time_elapsed)
        if time_elapsed == 1:
            #print(f'One')
            print(f'{time_elapsed}s')
            break
    while True:
        end=time.time()
        time_elapsed=(round(end-start,1))
        if time_elapsed == 2:
            end_sec=time.time()
            print(f'{time_elapsed}s')
            break
    while True:
        end=time.time()
        time_elapsed=(round(end-start,1))
        if time_elapsed == 3:
            print(f'{time_elapsed}s')
            break 


print('Show your hand in (seconds):')
countdown()




