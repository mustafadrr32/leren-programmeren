from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:
a = 9
robotArm.grab()
for q in range(8):
        color = robotArm.scan()
        if color == "red":
            for x in range(a):
                robotArm.moveRight()
                print(a)
            robotArm.drop()
            a -= 1
            for x in range(a):
                robotArm.moveLeft()
                
            robotArm.grab()  
        elif color != "red":
            a -= 1
            if color != "red":
                 robotArm.drop()
            robotArm.moveRight()  
            robotArm.grab()
        
robotArm.moveRight()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()