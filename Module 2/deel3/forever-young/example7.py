from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
for i in range(5):
    for x in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    if i <= 3:
        robotArm.moveRight()
        robotArm.moveRight()
robotArm.wait()


# Verplaats iedere stapel één plek naar links.

# Je mag maximaal 11 regels code gebruiken inclusief de import, het laden van de robotarm en de wait