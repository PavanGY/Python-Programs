command   = ""
started=False
while True:
    command=input("> ").lower()
    if command == "start":
        if started:
            print(" Are you Dumb,Its Already Started")
        else:
            started=True
            print("The Car Started")
    elif command == "stop":
        if not started:
            print("Come On Man, You Just Stopped It.")
        else:
            started=False
            print("The Car Stopped")
    elif command =="help":
        print("""
start - To start car
stop  - To stop car
Help  - To get info
""")
    elif command=="quit":
        break
    else:
        print("Sorry, I don't understand")
