#subway
import random
import csv
class player:
    name=""
    location = "centre"

    def jump():
        if obstacle.obstacle_name == "brick wall":
            return player.collision(False)
        elif obstacle.obstacle_name == "box":
            if player.location == obstacle.obstacle_position:
                return player.collision(False)
        else:
            return player.collision(True)

    def run():
        return print("Player running")
    

    def move_left():
        if player.location == "centre":
            player.location = "left"
            print("Player moved left")
            return obstacle.collision_imminent()
        elif player.location == "right":
            player.location = "centre"
            print("Player moved left")
            return obstacle.collision_imminent()


    def move_right():
        if player.location == "centre":
            player.location = "right"
            print("Player moved right")
            return obstacle.collision_imminent()
        elif player.location == "left":
            player.location = "centre"
            print("Player moved right")
            return obstacle.collision_imminent()


    def duck():
        if obstacle.obstacle_name == "bar":
            obstacle.collision(False)
            return print("You chose to duck the obstacle")
        else:
            return obstacle.collision_imminent()

    def collision(arg):
        if arg is True:
            return print(f"You have collided with the {obstacle.obstacle_name} obstacle in {obstacle.obstacle_position} path")
        else:
            return print(f"You evaded the {obstacle.obstacle_name} obstacle in the {obstacle.obstacle_position} path")
    pass
# collision_report =
# class path:
#     pass

# class pathright(path):
#     pass

# class pathleft(path):
#     pass

# class pathcentre(path):
#     pass


class obstacle:
    obstacle_name = ""
    obstacle_position = ""       
    


    def collision_imminent():
        if obstacle.obstacle_name == "brick wall" or "bar":
            return player.collision(True)
        elif obstacle.obstacle_name == "pole"and obstacle.obstacle_position == player.location:
            return player.collision(True)
        elif obstacle.obstacle_name == "box" and obstacle.obstacle_position == player.location:
            return player.collision(True)
        else:
            return player.collision(False)
        
    def obstruction():
        obs = [obstacle1, obstacle2, obstacle3, obstacle4]
        obs_choice = random.choice(obs)
        obstacle.obstacle_name = obs_choice.obstacle_name
        obstacle.obstacle_position = obs_choice.obstacle_position
        print("Obstacle Approaching")
        print("What would you like to do?")
        return

# *def obstacle_instances():
#     with open("subway_1.csv","w") as obs:
#         obs = csv.writer()*
obstacle1 = obstacle()
obstacle1.obstacle_name = "brick wall"

obstacle2 = obstacle()
obstacle2.obstacle_name = "box"
obstacle2.obstacle_position = "left"


obstacle3 = obstacle()
obstacle3.obstacle_name = "box"
obstacle3.obstacle_position = "right"

obstacle4 = obstacle()
obstacle4.obstacle_name = "box"
obstacle4.obstacle_position = "centre"

#obstacle_brick_wall = obstacle("brick wall","jump type","accross","large")
#obstacle_box_left = obstacle("box","jump type","left","medium")
#obstacle_box_right = obstacle("box", "jump type","right","medium")
#obstacle_box_centre = obstacle("box", "jump type", "centre","medium")
#obstacle_pole_left = obstacle("pole","side step", "left", "high")
#obstacle_pole_right = obstacle("pole","side step", "right", "high")
#obstacle_pole_centre = obstacle("pole","side step", "centre", "high")
#obstacle_long_bar = obstacle("bar","duck", "accross", "high")

#obstacle_select = [obstacle_brick_wall,obstacle_box_left,obstacle_box_right,obstacle_box_centre,obstacle_pole_left,obstacle_pole_right,obstacle_pole_centre,obstacle_long_bar]
#obstacle_select_count = len(obstacle_select)

#for i in obstacle_select:
#    print(random.choice(obstacle_select))
#     print(random.randint(0,i))
# # print(obstacle_brick_wall.obstacle_name)
# player.collision()

