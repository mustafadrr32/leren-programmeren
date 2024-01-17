from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
a = 1
robotArm.grab()
scan = robotArm.scan()
while scan != "":
    if scan == "":

        robotArm.drop()
    else:
        for y in range(a):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(a):
            robotArm.moveLeft()
        a += 1
    print(scan)
    robotArm.grab()
    scan = robotArm.scan()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()