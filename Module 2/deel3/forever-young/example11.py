from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
for x in range(9):
        robotArm.moveRight()    

for x in range(9):
       
        robotArm.moveLeft()
        robotArm.grab()
        color = robotArm.scan()
        if color == "white":
            robotArm.moveRight()
            robotArm.drop()
            robotArm.moveLeft()
        else:
            robotArm.drop()
        



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()