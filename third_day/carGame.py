command = ""
carStatus = False
while True:
    command = input("> ").lower()
    if command == "start":
        if carStatus:
            print("Car is already started")
        else:
            carStatus = True
            print("Car started...")
    elif command == "stop":
        if carStatus:
            print("Car stopped ..")
            carStatus = False
        else:
            print("Car is not running")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quite - to quite the game
        """)
    elif command == "quit":
        break
    else:
        print("sorry I don know")
