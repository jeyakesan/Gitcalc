started = False
while True:
    command = input(">").lower()
    if command == "help":
        print("""
    Start - to start the car
    Stop - to stop the car
    quit - to exit""")
    elif command == "start":
        if started:
            print ("The car is already started")
        else:
            print("The car is started ready to go!")
            started = True
    elif command == "stop":
        if not started:
            print ("the car is already stopped")
        else:
            print("The car is stopped")
            started = False
    elif command == "quit":
        break
    else:
        print("sorry i don't understand!")
