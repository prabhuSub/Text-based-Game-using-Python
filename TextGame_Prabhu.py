# Library imported:
# added comments by Prabhu 1

# Adding 2nd comment of Prabhu 1
# Adding comment Prabhu 2

import time;
import sys;
import pandas as pd;
import matplotlib.pyplot as plot
import numpy as np

def enter():
    input('''
    <Press ENTER>''')


def graph():
    global graphList
    graphList = [money, health, skills, ammo]
    N = len(graphList)
    x = range(N)
    width = 1/1.5
    plot.bar(x, graphList, width, color="blue")
    plot.show()
    plot.savefig("States_Report.png")

    #plot.plot(graphList)
    #plot.xlabel('Stats')
    #plot.ylabel('Numbers')
    #plot.show()
    #plot.savefig("States_Report.png")

    # my_df = pd.DataFrame(winnerList)
    # my_df.to_csv("Test.csv", index=False, header=False)
    # print(my_df)


def game():
    # Game begins executing from here.

    print('''
    *************************************************************************
    *                   Welcome to Adventure Text Game                      *
    *************************************************************************
         ___________              __                                  
         \__    ___/___ ___  ____/  |_     _________    _____   ____  
           |    |_/ __ |\  \/  /\   __\   / __ \__  \  /     \_/ __ \ 
           |    |\  ___/ >    <  |  |    / /_/  > __ \|  Y Y  \  ___/ 
           |____| \___  >__/\_ \ |__|    \___  (____  /__|_|  /\___  >
                      \/      \/        /_____/     \/      \/     \/ ''')
    time.sleep(3)
    print('''
    You are all set for an adventure.''')
    time.sleep(3)
    print('''
    Try to win this game by interacting at each point of time and by fulfilling few objectives as given''')
    time.sleep(3)
    enter()
    print('''
    The objectives are:
    
    1. Get trained by a friend
    2. Befriend a Dog
    3. Collect flowers
    4. Save a person from a situation
    5. Fight an elephant''')
    time.sleep(6)
    enter()
    print('''
    If you fulfill all the above objectives at any point of time in the game, You WIN!
    You can access the objectives whenever required in the game using "Stats"''')
    time.sleep(3)
    print('''
    Hope you enjoy and win it!''')
    time.sleep(3)
    print('''
    Have a great play!!!''')
    enter()

    # Variables set as global(so that can be accessed in other functions)
    # and initialised

    global money
    money = 0
    global health
    health = 10
    global fullhealth
    fullhealth = 10
    global skills
    skills = 0
    global attack
    attack = 0
    global ammo
    ammo = 0
    global winnerList
    winnerList = []
    global graphList
    graphList = []
    home()

def winner():
    # Winner() is the function used for adding up all the winning factors of the player.
    # Called at every winning steps to check if the winning condition is satisfied.
    global money
    global health
    global skills
    global ammo
    global winnerList
    global graphList

    #print(winnerList)
    if 'Trained' in winnerList:
        #print("ok. Trained")
        if 'dog' in winnerList:
            #print("ok. dog")
            if 'flowers' in winnerList:
                #print("ok. flowers")
                if 'save' in winnerList:
                    #print("ok. save")
                    if 'fight' in winnerList:
                        time.sleep(3)
                        print('''
    ******************************************************
    *                 CONGRATULATIONS!!!!                *
    ******************************************************
    Surprisingly, you have fulfilled all the objectives 
              of this game with your strategies!
    ******************************************************
                                                 __ 
          __ __ _____ _____    _ _ _ _____ _____|  |
         |  |  |     |  |  |  | | | |     |   | |  |
         |_   _|  |  |  |  |  | | | |  |  | | | |__|
           |_| |_____|_____|  |_____|_____|_|___|__|
                                                    
    ******************************************************''')
                        print('''
    You won the game with below stats:''')
                        time.sleep(3)
                        stats()
                        # graph plot
                        graph()
                        sys.exit()
                    else:
                        return
                else:
                    return
            else:
                return
        else:
            return
    else:
        return



def home():
    # Initial room from where player starts

    global health
    global money
    print('''***********************
                         `'::.
                    _________H ,%%&%,
                   /\     _   \%&&%%&%
                  /  \___/^\___\%&%%&&
                  |  | []   [] |%\Y&%'
                  |  |   .-.   | ||  
                ~~@._|@@_|||_@@|~||~~~~~~~~~~~~~
                     `""") )"""`
    You are inside your house. Choose the options to interact:
    1. Go out to the streets
    2. Take rest
    3. Get money
    4. Stats''')
    time.sleep(1)
    choice = prompt()
    if choice == "1":
        street()
    elif choice == "2":
        health = fullhealth
        time.sleep(3)
        print('''**************
    You took enough rest. Your health is fully charged''')
        health = fullhealth
        print('''
    health: ''', health)
        time.sleep(3)
        home()
    elif choice == "3":
        time.sleep(1)
        money = int(input('''
    How much money do you want = $'''))
        time.sleep(1)
        print('''
    Money: ''', money)
        time.sleep(1)
        home()
    elif choice == "4":
        stats()
        time.sleep(3)
        home()
    else:
        home()

def stats():
    # stats() is the function called to display the stats
    # of the player when called by user during the game

    print('''***********
    The OBJECTIVES were to:
    1. Get trained by a friend
    2. Befriend a Dog
    3. Collect flowers
    4. Save a person from a situation
    5. Fight an elephant\n''')
    print("    Money:", money)
    print("    health:", health)
    print("    skills:", skills)
    print("    Ammo:", ammo)
    print('''***********''')
    enter()

def prompt():
    # Used for user input
    x = input('''Type a command:''')
    return x

def friendHouse():
    # Friend's house for user to interact

    global skills
    global money
    global winnerList
    print('''*************
                   _
                 _|=|__________
                /              \Friend's
               /                \House
              /__________________\.
               ||  || /--\ ||  ||
               ||[]|| | .| ||[]||
             ()||__||_|__|_||__||()
            ( )|-|-|-|====|-|-|-|( ) 
            ^^^^^^^^^^====^^^^^^^^^^^
    You are at your friends house. Choose the options:
    1. Health refill
    2. Training
    3. Back to Street
    4. Stats''')
    time.sleep(1)
    choice = prompt()
    if choice == "1":
        health = fullhealth
        print('''
    health: ''', health)
        time.sleep(3)
        friendHouse()
    elif choice == "2":
        time.sleep(3)
        if money == 0:
            print('''
    Sorry, you have no money to get trained! Return with money to get trained.
    Not a generous friend of yours!!! :P ''')
            time.sleep(3)
            friendHouse()
        else:
            winnerList.append('Trained')
            print('''***********
                        +-+-+-+-+-+-+-+
                        |T|R|A|I|N|E|D|
                        +-+-+-+-+-+-+-+''')
            print('''
    You got trained. Money spent reduces by 1. Skills added is 1''')
            skills = skills + 1
            money = money - 1
            time.sleep(3)
            print('''
    Skills: ''', skills)
            time.sleep(3)
            print('''
    Money: ''', money)
            time.sleep(3)
            winner()
            friendHouse()
    elif choice == "3":
        street()
    elif choice == "4":
        time.sleep(3)
        stats()
        time.sleep(3)
        friendHouse()
    else:
        friendHouse()

def fight():
    # Fight occurs when player chooses it.

    global ammo
    global winnerList
    print('''
    *********************************
                            ____
                       .---'-    \E
          .-----------/           \E
         /           (         ^  |   __
    &   (             \        O  /  / .'
    '._/(              '-'  (.   (_.' /
         \                    \     ./
          |    |       |    |/ '._.'
           )   @).____\|  @ |
       .  /    /       (    |   
      \|, '_:::\  . ..  '_:::\ ..\).
      
    There is a mad Elephant behind you:
    1. Fight it
    2. Run away
    ******************************''')
    time.sleep(1)
    choice = prompt()
    if choice == "1":
        if ammo == 0:
            time.sleep(3)
            print('''****************
    You had 0 Ammo
    You are killed as you had no Ammo
    Your stats at the end of the game''')
            time.sleep(3)
            stats()
            time.sleep(3)
            print('''                                   __ 
     _____ _____ _____ _____    _____ _____ _____ _____|  |
    |   __|  _  |     |   __|  |     |  |  |   __| __  |  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|__|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|__|''')
            graph()
        else:
            time.sleep(3)
            winnerList.append('fight')
            print('''
    You used the stones to scare away the elephant. Ammo reduces by 1''')
            ammo = ammo - 1
            time.sleep(3)
            print('''
    Ammo: ''', ammo)
            time.sleep(3)
            winner()
            fight()
    else:
        forest()


def forest():
    # Forest in another room the player enters

    global health
    global ammo
    global attack

    # If the player enters forest for first time,
    # he is attacked by the BEAR to make it dynamic

    if attack == 0:
        print('''
    ***********************************
    You are in a dense forest. Look out as a bear is approaching!''')
        time.sleep(3)
        print('''
               .--.              .--.
              : (\ ". _......_ ." /) :
               '.    `        `    .'
                /'   _        _   `\Bear
               /     0}      {0     \Bear
              |       /      \       |
              |     /'        `\     |
               \   | .  .==.  . |   /
                '._ \.' \__/ './ _.'
                /  ``V._-''-_.V``  \Bear''')
        time.sleep(3)
        print('''   
    OH NO!''')
        time.sleep(3)
        print('''
    The bear attacked you''')
        health = health - 3
        attack = 1
        time.sleep(3)
        print('''******************
    Your health got reduced by 3
    Health: ''', health)
        time.sleep(3)
        forest()
    else:
        print('''*********************************
         #o#                                #o#
       ####o#                              ####o#
     #o# \#|_#,#                         #o# \#|_#,#
    ###\ |/   #o#        FOREST         ###\ |/   #o#
     # {}{      #                        # {}{      #
       }{{                                 }{{
     ,'  `                               ,'  `
   You are in the Forest. Choose your options:
    1. Pick up stones
    2. Go deep inside the forest
    3. Go to the flooded River
    4. Go back to Street
    5. Stats''')
        time.sleep(1)
        choice = prompt()
        if choice == "1":
            ammo = ammo + 1
            print('''******************
    You have picked up a stone. Your ammo increases by 1
    Ammo: ''', ammo)
            time.sleep(3)
            forest()
        elif choice == "2":
            fight()
        elif choice == "3":
            time.sleep(3)
            print('''*******************
    Sorry, you got drowned into the flooded river.
                                               __ 
     ____  _____ _____ _ _ _ _____ _____ ____ |  |
    |    \| __  |     | | | |   | |   __|    \|  |
    |  |  |    -|  |  | | | | | | |   __|  |  |__|
    |____/|__|__|_____|_____|_|___|_____|____/|__|
     
    Your stats at the end of the game''')
            time.sleep(3)
            stats()
            time.sleep(3)
            print('''
                                                        __
     _____ _____ _____ _____    _____ _____ _____ _____|  |
    |   __|  _  |     |   __|  |     |  |  |   __| __  |  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|__|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|__|
    ''')
            graph()
        elif choice == "4":
            time.sleep(3)
            street()
        elif choice == "5":
            stats()
            time.sleep(3)
            forest()
        else:
            forest()


def park():
    # Park in another room to interact in the game when choosen.

    global ammo
    global skills
    global health
    global winnerList
    print('''**********************
                    ___   ___    ___   _  __  
                   | _ \ /   \  | _ \ | |/ /  
                   |  _/ | - |  |   / | ' <   
                  _|_|_  |_|_|  |_|_\ |_|\_\  
                _| """ _|"""""_|"""""_|"""""| 
                "`-0-0-"`-0-0-"`-0-0-"`-0-0-' 
    You are in the park sitting on a bench enjoying the view. Go ahead with the choices:
    1. Pick up a stone
    2. Dog fight
    3. Fight with a guy bullying
    4. Go back to Streets
    5. Stats''')
    time.sleep(1)
    choice = prompt()
    if choice == "1":
        ammo = ammo + 1
        print('''****************
    You have picked up a stone. Your ammo increases by 1
    Ammo: ''', ammo)
        time.sleep(3)
        park()
    elif choice == "2":
        print('''****************
                    ___
                 __/_  `.  .-"""-.
                 \_,` | \-'  /   )`-')
                  "") `"`    \  ((`"`
                 ___Y  ,    .'7 /|
                (_,___/...-` (_/_/ 
    A dog is trying to disturb you in the park
    Choose the options:
    1. Use stone
    2. Befriend the dog
    ''')
        time.sleep(1)
        choice = prompt()
        if choice == "1":
            if ammo > 0:
                ammo = ammo - 1
                if skills > 0:
                    skills = skills - 1
                else:
                    skills = 0
                    time.sleep(3)
                print('''***************
    The dog runs away. Ammo and Skills reduces by 1''')
                time.sleep(3)
                print('''
    Ammo: ''', ammo)
                time.sleep(3)
                print('''
    Skills: ''', skills)
                time.sleep(3)
                park()
            else:
                health = health - 1
                time.sleep(3)
            print('''*******************
    As your are low with Ammo. The dog bites you. Health reduces by 1
    health: ''', health)
            time.sleep(3)
            park()
        elif choice == "2":
            if skills > 0:
                skills = skills - 1
            else:
                skills = 0
            winnerList.append('dog')
            time.sleep(3)
            print('''******************
    You befriend the dog. Its your friend now''')
            time.sleep(3)
            print('''
         |\_/|                  
         | @ @   Woof! 
         |   <>              _  
         |  _/\------____ ((| |))
         |               `--' |   
     ____|_       ___|   |___.' 
    /_/_____/____/_______| ''')
            time.sleep(3)
            print('''
    Skill reduces by 1 as you used it to pet
    Skills: ''', skills)
            winner()
            time.sleep(3)
            park()
    elif choice == "3":
        time.sleep(3)
        print('''********************
    A guys is bullying an innocent boy in the Park.
    1. Try to save him
    2. Ignore it
    *********************************    
    3. Collect the Flowers around ;)(its hidden over here)''')
        time.sleep(1)
        choice = prompt()
        if choice == "1":
            health = health - 1
            winnerList.append('save')
            print('''******************
    That's a heroic job you have done. WELL DONE!!!
    Skills set to 10, though Health reduced by 1''')
            time.sleep(3)
            skills = 10
            print('''
    Health: ''', health)
            time.sleep(3)
            print('''
    Skills: ''', skills)
            winner()
            time.sleep(3)
            park()
        elif choice == '2':
            skills = 0
            print('''******************
    Your skills reduced to 0
    Skills: ''', skills)
            time.sleep(3)
            park()
        elif choice == '3':
            winnerList.append('flowers')
            time.sleep(3)
            print('''
    Finally! You have collected the flowers''')
            print('''
                    _____
                  /  ___  \Flower
                /  /  _  \  \Flower
              /( /( /(_)\ )\ )\Flower
             (  \  \ ___ /  /  )
             (    \ _____ /    )
             /(               )\Flower
            |  \             /  |
            |    \ _______ /    |
             \    / \   / \    /
               \/    | |    \/
                     | | 
                     | |
                     | |''')
            winner()
            time.sleep(3)
            street()
    elif choice == "4":
        time.sleep(3)
        park()
    elif choice == "5":
        stats()
        time.sleep(3)
        park()


def street():
    # Street is the second room for the player to enter.

    global ammo
    print('''********************
        ___  ,--.  __________________________/   ,   /_______
            'O---O'~
         _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   ,--.   _ _ _ _ _
                 _____                       ~'O---O'
         _______< Rome|_____        __________________________
                   ||      /   ,   /
    You are in the streets. Select the options:
    1. Go to the Park
    2. Go to Friends house
    3. Go to Forest
    4. Pick up a stone
    5. Go home
    6. Stats''')
    time.sleep(1)
    choice = prompt()
    if choice == "1":
        time.sleep(3)
        park()
    elif choice == "2":
        time.sleep(3)
        friendHouse()
    elif choice == "3":
        time.sleep(3)
        forest()
    elif choice == "4":
        ammo = ammo +1
        time.sleep(3)
        print('''*******************
    You have picked up a stone. Your ammo increases by 1
    Ammo: ''', ammo)
        time.sleep(3)
        street()
    elif choice == "5":
        time.sleep(3)
        home()
    elif choice == "6":
        stats()
        time.sleep(3)
        street()
    else:
        street()

# Game is initialised below
game()

