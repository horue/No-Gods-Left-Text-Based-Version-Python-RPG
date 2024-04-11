import cmd
import textwrap
import sys
import os
import time
import random


screen_width=100

class player:
    def __init__(self):
        self.name=''
        self.inventory=[]
finalPlayer=player()

def title_screen_menu():
    option=input("> ")
    if option.lower() ==("play"):
        sys.exit #start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a command.")
        option=input("> ")
        return
    
def title_screen():
    print("#"*len('# Welcome to No Gods Left. #'))
    print('# Welcome to No Gods Left. #')
    print("#"*len('# Welcome to No Gods Left. #'))
    print('Play')
    print('Help')
    print('Quit')
    print('Made by horue.')
    title_screen_menu()


def help_menu():
    print("#" * 30)
    print('# No Gods Left - Help Screen. #')
    print("#" * 30)
    print('— Use actions like look and interact')
    print("— Use move to go to the next room when you're done")
    print('— Have fun!')
    print('Made by horue.')
    return(title_screen)


title_screen()