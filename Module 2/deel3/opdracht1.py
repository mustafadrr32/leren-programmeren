import time

x = 31

while x > 0:
    x -= 1
    time.sleep(1)
    print(x)
    if x == 0:
        print("racketlancering!")