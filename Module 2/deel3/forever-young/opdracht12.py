from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:
a = 9
for q in range(9):
        robotArm.grab() 
        color = robotArm.scan()
        if color == "red":
            for x in range(a):
                
                robotArm.moveRight()
                print(a)
            robotArm.drop()
            a -= 1
            for x in range(a):
                robotArm.moveLeft()
                
             
        elif color != "red":
            a -= 1
            if color != "red":
                 robotArm.drop()
                 robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()