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
    print("#"*len('# No Gods Left. #'))
    print('# No Gods Left. #')
    print("#"*len('# No Gods Left. #'))
    print('Novo Jogo')
    print('Continuar')
    print('Ajuda')
    print('Sair')
    print('Feito por horue.')
    title_screen_menu()


def help_menu():
    print("#" * len('# No Gods Left - Tela de Ajuda. #'))
    print('# No Gods Left - Tela de Ajuda. #')
    print("#" * len('# No Gods Left - Tela de Ajuda. #'))
    print('— Use as ações sugeridas para contiunar o jogo')
    print("— Use 'falar' para interagir com algum personagem")
    print('— Se divirta!')
    print('Feito por horue.')
    return(title_screen)


title_screen()