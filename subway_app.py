import time
from subway import player
from subway import obstacle



class subwayapp:
    def start():
        print("starting app....")
        print("loading")
        time.sleep(1.0)
        print("loading")
        time.sleep(1.0)
    
        print("""when player meets a brick wall  player should jump
              when player meets a bar (across the playing paths) player should duck
             when player meets a pole player can either turn left or right dpending on the path of the pole
             when player meets a box player can either turn left or right depending on the path of the pole""")
        time.sleep(3.0)
        
subwayapp.start()
print (player.location)
time.sleep(6.0)
player_name = input("enter name to start game: ")
print("starting")
time.sleep(2.0)
print(f"starting game with player {player_name}")
time.sleep(4.0)
player.run()
time.sleep(2.2)


def player_location():
    if player.location == "centre":
       print("[1] move_left()")
       print("[2] move_right()")
       print("[3] jump()")
       print("[4] duck ()")
       print("[5] exit()")

    elif player.location== "left":
        print("[1] move_right()")
        print("[2] jump()")
        print("[3] duck ()")
        print("[4] exit()")

    elif player.location== "right":
        print("[1] move_left()")
        print("[2] jump()")
        print("[3] duck ()")
        print("[4] exit()")

    



player.location="centre"    
player_location()
while True:
    try:
        option = int(input("enter your option: "))
    except ValueError:
        print("please try again")
        continue
    else:
        if option==1:
            #do option 1 stuff
            break
        elif option==2:
            #do option 2 stuff
            break
        elif option==3:
            #do option 3 stuff
            break
        elif option==4:
            #do option 4 stuff
            break
        elif option==5:
             # do option 5 tuff
             exit()
        else:
             continue
            

        


   
  




    




#while True:
#   if player == obstacle:
#        print("move_left")
 #   else:
 #       print("you hit an {obstacle}")
         


