from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
for x in range(9):
        robotArm.moveRight()
aantal = 0

    
    

for x in range(9):
        aantal += 1
        for x in range(1):
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