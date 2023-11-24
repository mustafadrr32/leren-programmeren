from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

for i in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()


robotArm.wait()
