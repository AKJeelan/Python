help_command = "help"
start_command = "start"
stop_command = "stop"
quit_command = "quit"
started = False

while True:
    command = input(">").lower()
    if command == help_command:
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == start_command:
        if started:
            print("Car already started...")
        else:
            print("Car started... Ready to go!")
            started = True
    elif command == stop_command:
        if not started:
             print("Car already stopped...")
        else:
            print("Car Stopped.")
            started = False
    elif command == quit_command:
            break
    else:
        print("I dont't understand that...")



