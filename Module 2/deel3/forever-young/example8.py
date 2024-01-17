from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
#robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
for y in range(7):
    robotArm.grab()
    for x in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(8):
        robotArm.moveLeft()

robotArm.wait()


# Na jouw code wachten tot het sluiten van de window:
# robotArm.wait()
# Verplaats de stapel naar de rechterkant.

# Je mag maximaal 11 regels code gebruiken inclusief de import, het laden van de robotarm en de wait
