command=""
started = False
stopped = False
while True:
    command = input(">").lower()
    if command =='start':
        if started:
            print("car is already running")
        else:
            print('car started...')
            started=True
        
    elif command =='stop':
        if stopped :
            print('Car is already stopped')

        else:
            print('car stopped')
            stopped = True

    elif command== 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')

    elif command== 'quit':
        break

    else:
        print('I dont understand')
