command = input("> ")
       
i=0

while command.upper()!= 'QUIT':
    if command.upper() == 'START':
        if i==1:
            print("Car was alredy started")
        else :
            i=1
            print("Car started")


    elif command.upper() == 'STOP':
        if i==0:
            print("Car was alredy stopped")
        else:
            i=0
            print("The car has stopped")

    else :
        print("Aukat me raho")
    command = input('> ')

