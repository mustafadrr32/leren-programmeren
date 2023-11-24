from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

robotArm.grab()

for i in range(2):
    robotArm.moveRight()


robotArm.drop()

for i in range(2):
    robotArm.moveLeft()


robotArm.grab()

for i in range(3):
    robotArm.moveRight()



robotArm.drop()

for i in range(3):
    robotArm.moveLeft()

robotArm.grab()

for i in range(4):
    robotArm.moveRight()

robotArm.drop()

for i in range(4):
    robotArm.moveLeft()
robotArm.grab()

for i in range(5):
    robotArm.moveRight()

robotArm.drop()

for i in range(5):
    robotArm.moveLeft()


robotArm.grab()
robotArm.moveRight()
robotArm.drop()

robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

for i in range(3):
    robotArm.moveRight()

robotArm.grab()

for i in range(3):
    robotArm.moveLeft()

robotArm.drop()

for i in range(2):
    robotArm.moveRight()

robotArm.grab()

for i in range(2):
    robotArm.moveLeft()
    
robotArm.drop()

for i in range(4):
    robotArm.moveRight()

robotArm.grab()

for i in range(4):
    robotArm.moveLeft()

robotArm.drop()

robotArm.speed = 9


robotArm.wait()
