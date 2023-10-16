import time
from subway_1 import player
from subway_1 import obstacle
import csv
import random



class subwayapp:
    def start():
        print("starting app....")
        print("loading")
        time.sleep(1.0)
        print("loading")
        time.sleep(1.0)
    
        print("""WELCOME TO THE OBSTACLE GUESSING GAME\n
        OBSTACLES OF TYPE BOX, POLE, BRICK WALL AND BAR WILL APPROACH PLAYER\n
        PLAYER WILL HAVE TO EVADE OBSTACLE USING AVAILABLE CHOICES IN THE LIST PROVIDED\n
        PLAYER CAN EXIT GAME USING THE EXIT OPTION IN CHOICES AVAILABLE\n
        HOW LUCKY ARE YOU??\n
        HOW MANY OBSTACLES CAN YOU EVADE???\n
        HAVE FUN!!!!""")
        time.sleep(3.0)
        

player.location == "centre"

# This function is called when player is in centre path 
def player_centre():
        print("[1] move_left()")
        print("[2] move_right()")
        print("[3] jump()")
        print("[4] duck ()")
        print("[5] exit()")
        try:
            option = int(input("what's your choice: "))
        except ValueError:
                print("please try again")
        if option==1:
            player.move_left()
        elif option==2:
            player.move_right()
        elif option==3:
            player.jump()
        elif option==4:
            player.duck()
        elif option==5:
             # do option 5 tuff
            exit()
        else:
            print("Please choose one of the options in the list above")
        

# This function is called when player is in left path 
def player_left():
        print("[1] move_right()")
        print("[2] jump()")
        print("[3] duck ()")
        print("[4] exit()")
        try:
                option = int(input("choose which path to take: "))
        except ValueError:
            print("please try again")
        else:        
            if option==1:
                player.move_right()
            elif option==2:
                player.jump()
            elif option==3:
                player.duck()
            else:
                print("Please choose one of the options in the list above")
        

# This function is called when player is in right path 
def player_right():
        print("[1] move_left()")
        print("[2] jump()")
        print("[3] duck ()")
        print("[4] exit()")
        try:
            option = int(input("choose which path to take: "))
        except ValueError:
            print("please try again")
        else:        
            if option==1:
                player.move_left()
            elif option==2:
                player.jump()
            elif option==3:
                player.duck()
            else:
                print("Please choose one of the options in the list above")

# This is the choice player makes when obstacle is approaching
# Player will have to guess what obstacle and make a decision
def player_action():
    if player.location == "centre":
        player_centre()
    elif player.location == "left" :
        player_left()
    elif player.location == "right":
        player_right()


# GAME STARTS HERE
subwayapp.start()
time.sleep(6.0)
# RECEIVING PLAYER'S NAME
player_name = input("enter name to start game: ")
time.sleep(2.0)
print(f"starting game with player {player_name}")
time.sleep(3.2)
print (f"Player is in {player.location} path")
player.run()
time.sleep(2.0)
while True:
    obstacle.obstruction()
    time.sleep(2.0)
    player_action()

    

# def obstruction_extract():
#     with open("subway.csv", "w") as extract:
#         records = csv.reader(extract)
#         name, types, position, size = records
#         record = random.choice(records)
#         if record.name == "brick wall":