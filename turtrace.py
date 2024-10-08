import turtle
import random

screen=turtle.Screen()
screen.setup(width=500,height=500)
colors=["red","green","black","blue","purple"]
turtles=["timmy","jimmy","sunny","brownie","rocky"]
len_y=[0,90,180,-90,-180]
objturtles=[]
 
def create_turtles():
    for p in range(len(turtles)):
        turtles[p]=turtle.Turtle("turtle")
        objturtles.append(turtles[p])  
        objturtles[p].penup()       
        objturtles[p].color(colors[p])  
        objturtles[p].goto(x=-230,y=len_y[p])
create_turtles()  
             
player_choice=turtle.textinput("color","color a turtle which will win!?")

if player_choice:        
    start_race=True
    
while start_race:      
    for move in (objturtles):
        randnum=random.randint(0,20)
        move.forward(randnum)
        if move.xcor()>230:
            start_race=False
            if move.pencolor()==player_choice:
                print(move.pencolor())
                print(f"hey!,{move.pencolor()} won the race, you choose {player_choice}")
            else:
                print(f"{move.pencolor()} won the race, you choose {player_choice}")
              

















screen.exitonclick()