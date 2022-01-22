import termcolor, sys, os, json, random

from torch import normal, true_divide

Data = {'new': True, 'land': None, 'village': None, 'clan': None, 'right eye': 'normal', 'left eye': 'normal'}
clanList = []
villageList = []
landList = []
elementList = []


def welcomeScreen():
    global Data
    termcolor.cprint("########", 'green')
    termcolor.cprint("--Play--", 'blue')
    termcolor.cprint("--Quit--", 'red')
    termcolor.cprint("########", 'green')
    answer = input(">>>   ")
    while answer.lower() not in ['play', 'quit']:
        termcolor.cprint("Bad command, try again...", 'red')
        answer = input(">>>   ")
    if answer.lower() == 'quit':
        sys.exit()
    if answer.lower() == 'play':
        termcolor.cprint("############", 'green')
        termcolor.cprint("--New game--", 'grey')
        termcolor.cprint("--Load game-", 'grey')
        termcolor.cprint("############", 'green')
        answer = input(">>>   ")
        while answer.lower() not in ['new game', 'load game', 'load', 'new']:
            termcolor.cprint("Bad command, try again...", 'red')
            answer = input(">>>   ")
        if answer in ['new game', 'new']:
            main()
        if answer in ['load game', 'load']:
            if not os.path.exists("save.json"):
                termcolor.cprint("No savefile found, starting new game...", 'red')
                main()
            with open('save.json', 'r') as savefile:
                Data = json.load(savefile)
            main()

def main():
    global Data
    if Data['new']:

    while True: