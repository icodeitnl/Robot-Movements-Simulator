import math
#Simulator of the robot movements uses manual imput of directions,turns and steps. Enables curve trajectory.
#Launching through "advance" function call.
class Robot(object):

    def __init__ (self,d,x,y):
        self.d=d
        self.x=x
        self.y=y
        step={self.x,self.y}

    def advance(self):
        path=[]
        while True:
            turn=input("Which direction do you want me to go?" )
            if turn in self.d:
                print (f"Turning {turn}")
                path.append(turn)
                print (path)
            if turn not in self.d:
                turn=input("Please type in the Cardinal Directions: ")
                if turn in self.  d:
                    print (f"Turning {turn}")
                    path.append(turn)
                    print (path)    
                move=int(input("How many moves do you want me to make?"))
                if "north" in path[-1:]:
                    step={self.x,move+self.y}
                    path.append(step)
                    print(path)
                if "south" in path[-1:]:
                    step={self.x,self.y-move}
                    path.append(step)
                    print(path)
                if "east" in path[-1:]:
                    step={self.x+move,self.y}
                    path.append(step)
                    print(path)
                if "west" in path[-1:]:
                    step={self.x-move,self.y}
                    path.append(step)
                    print(path)
                side=input("Do I turn left or right?")
                path.append(side)
                curve=input(f"How much degrees should I turn?")
                if "right" in side:
                    turn_right_degrees=math.sin(math.radians(self.y))                  
                    print (f"Turning {turn_right_degrees}")
                    path.append(turn_right_degrees)
                    print(path)
                if "left" in side:
                    turn_left_degrees=math.cos(math.radians(self.x))
                    print (f"Turning {turn_left_degrees}")
                    path.append(turn_left_degrees)  
                    print(path)
                    if input == "":
                        break
launch=Robot({"north","south","east","west"},7,3)
launch.advance()  

#Simulator of the robot movements uses manual imput of directions,turns and steps. Enables curve trajectory.
#Launching through the "Robot"class call.
class Robot(object):

    def __init__ (self,d,x,y):
      
        path=[]
        step={x,y}   
        while True:
            turn=input("Which direction do you want me to go? " )
            if turn in d:
                print (f"Turning {turn}")
                path.append(turn)
                print (path)
            if turn not in d:
                turn=input("Please type in the Cardinal Directions: ")
                if turn in d:
                    print (f"Turning {turn}")
                    path.append(turn)
                    print (path)

                    move=int(input("How many moves do you want me to make? "))
                    if "north" in path[-1:]:
                        step={x,move+y}
                        path.append(step)
                        print(path)
                    if "south" in path[-1:]:
                        step={x,y-move}
                        path.append(step)
                        print(path)
                    if "east" in path[-1:]:
                        step={x+move,y}
                        path.append(step)
                        print(path)
                    if "west" in path[-1:]:
                        step={x-move,y}
                        path.append(step)
                        print(path)
                    side=input("Do I turn left or right? ")
                    path.append(side)
                    curve=input(f"How much degrees should I turn? ")
                    if "right" in side:
                        turn_right_degrees=math.sin(math.radians(y))                  
                        print (f"Turning {turn_right_degrees}")
                        path.append(turn_right_degrees)
                        print(path)
                    if "left" in side:
                        turn_left_degrees=math.cos(math.radians(x))
                        print (f"Turning {turn_left_degrees}")
                        path.append(turn_left_degrees)  
                        print(path)
                        if input == "":
                            break 
Robot({"north","south","east","west"},7,3)
 

