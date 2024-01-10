from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:

a1 = 10

for x in range(5):
    
        a1 -= 1
        robotArm.grab()
        
        for k in range(a1):
            robotArm.moveRight()
        a1 -= 1 
        robotArm.drop()
        for y in range(a1):
            robotArm.moveLeft()
        
        


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()