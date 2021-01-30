airline = input("Airline ").upper()
depart = input("Departure ").title()
destin = input("Destination ").title()
seats = int(input("No. of seats "))

for i in range(seats+1):
    print(f'{airline}:{depart[:3]}:{destin[:3]}:{(101+i)}')

