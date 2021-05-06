# Considering only 20 total seats available
# Maximum of 30 seats in possible in queue (waiting list)
# uin = unique identity number given to each new user
# name_list = [[uin1,name1],[uin2,name2],....]
# seat_list = [uin1,uin2,uin3......]
# waiting_list = [[uin1,number_of_seats1],[uin2,number_of_seats2]....]

import time
from random import randint


TOTAL_SEATS = 20 
WAITING_SEATS = 30
MAX_SEAT_PER_UIN = 4


def check_user():
    print("Hello there !")

    reply = input("Are you a new user ? (y/n) ")
    if reply == "y" :
        new_user()
    else :
        login(name_list)


def login(name_list):
    
    uin = input("Enter your UIN number : ")

    if uin == "ADMIN001" :
        print("Current seat status : ",seat_booked_view(seat_list))
        print("Waiting seats : ",waiting_seat_list)
        print("All users : ",name_list)
        check_user()

    file = open("data.txt" ,"r")
    name_list = file.readlines()

    for i in name_list: 
        if i[:8] == uin :
            print("Hello",i[9:])
            name = i[9:]
            user_choice(uin,name)

    check_user()


def new_user():
    name = input("Enter name : ")
    if len(name) < 3 :
        print("Name should be atleast 3 character")
        new_user()

    uin = name[0:3].upper() + str(randint(20000,29999))
    print("Your UIN is :",uin)

    file = open("data.txt", "a")
    file.write(f"{uin}:{name}\n")
    file.close()
    user_choice(uin,name)


def user_choice(uin,name):

    k = int(input("""Enter choice --> 
    1 : Seat Booking
    2 : Seat cancellation
    3 : Booking Status
    4 : Empty seats available
    5 : Exit\n  """))

    if(k == 1) : 
        seat_booked_view(seat_list)
        seat_booking(seat_list,uin,name)

    elif(k == 2):
        seat_cancelling(seat_list,waiting_seat_list,uin,name)

    elif(k == 3):
        seat_status(uin,name)
    
    elif(k == 4):
        seat_booked_view(seat_list)

    elif(k == 5):
        check_user()

    else:
        print("Incorrect input ")
        user_choice(uin,name)


def seat_booked_view(seat_list):
    print("""     E = Empty , R = Booked seat""")

    for i in range(TOTAL_SEATS//2):
        if seat_list[i] == 0 and seat_list[i+10] == 0:
            print(f"E {i+1}\t E {i+11}")
        elif seat_list[i] != 0 and  seat_list[i+10] == 0:
            print(f"R {i+1}\t E {i+11}")
        elif seat_list[i] == 0 and  seat_list[i+10] != 0:
            print(f"E {i+1}\t R {i+11}")
        else :
            print(f"R {i+1}\t R {i+11} ")

        if i == 4 :
            print("\n")

def seat_booking(seat_list,uin,name):

    empty_seat = 0
    booked_seats = 0

    for i in range(TOTAL_SEATS):
        if seat_list[i] == 0:
            empty_seat += 1
        if seat_list[i] == uin :
            booked_seats += 1


    if empty_seat != 0 and booked_seats < MAX_SEAT_PER_UIN:
        choice = int(input("Choose seat to book (0 to return) "))
        if(choice <= TOTAL_SEATS and choice >= 1 and seat_list[choice-1] == 0 ):
            print("Seat confirmed :")
            seat_list[choice-1] = uin
            print(f"Name : {name}\t UIN : {uin}\t Seat number : {choice}")

            booked_seats += 1
            while(booked_seats < MAX_SEAT_PER_UIN and input("\nBook more seat ? (y/n) ") == "y" ) :
                choice = int(input("Choose seat to book (0 to return) "))
                if(choice <= TOTAL_SEATS and choice >= 1 and seat_list[choice-1] == 0 ):
                    time.sleep(1)
                    print("Seat confirmed ")
                    seat_list[choice-1] = uin
                    print(f"Name : {name}\t UIN : {uin}\t Seat number : {choice}")
                    booked_seats += 1
                    empty_seat -= 1


                elif  seat_list[choice-1] != 0:
                    print("This seat is already booked")

                if empty_seat == 0:
                    waiting_seat_booking(waiting_seat_list,uin,name)

            if booked_seats == MAX_SEAT_PER_UIN :
                time.sleep(1)
                print("You have booked maximum (10) possible seats under this UIN")

        elif choice == 0  :
            user_choice(uin,name)
        
        else :
            print("Please choose a valid seat ")
            seat_booking(seat_list,uin,name)

    elif booked_seats == MAX_SEAT_PER_UIN:

        print("You have alredy booked maximum (10) number of seats for this UIN")
    else :
        waiting_seat_booking(waiting_seat_list,uin,name)

    time.sleep(2)
    user_choice(uin,name)

def waiting_seat_booking(waiting_seat_list,uin,name):

    print("No seat available")

    already_booked = False
    for i in range(len(waiting_seat_list)):
        if waiting_seat_list[i][0] == uin :
            already_booked = True
            break

    if input("Book seat under waiting list (y/n) ?") == "y":
        if already_booked and waiting_seat_list[i][1] < MAX_SEAT_PER_UIN:
            number_of_seats = int(input(f"How many seats ? (Maximum of { 10-waiting_seat_list[i][1]}) : "))
            if number_of_seats <= MAX_SEAT_PER_UIN-waiting_seat_list[i][1]:    
                waiting_seat_list[i][1] += number_of_seats  
            else :
                print("You are trying to book too many seats")
                print("Maximum of only 10 seats")
                waiting_seat_booking(waiting_seat_list,uin,name)

        elif already_booked == False :
            number_of_seats = int(input("How many seats ? (Maximum of 10) : "))
            if number_of_seats <= MAX_SEAT_PER_UIN :    
                waiting_seat_list.append([uin,number_of_seats])
                print(f"{number_of_seats} seats confirmed. ")
            else :
                print("You are trying to book too many seats")
                print("Maximum of only 10 seats")
                waiting_seat_booking(waiting_seat_list,uin,name)
        else :
            print("You are trying to book too many seats")
            print("Maximum of only 10 seats")
            waiting_seat_booking(waiting_seat_list,uin,name)
    
    time.sleep(1)
    user_choice(uin,name)


def seat_cancelling(seat_list,waiting_seat_list,uin,name):

    seat_booked_view(seat_list)
    
    seat_booked = False 
    for i in range(TOTAL_SEATS):
        if seat_list[i] == uin :
            print(f"Seat number {i+1}")
            seat_booked = True

    if seat_booked:
        while(input("Cancel your seat ? (y/n) ") == "y"):
            seat_to_cancel = int(input("Which seat do you wish to cancel ? (0 to return)"))
            if seat_to_cancel > 0 and seat_list[seat_to_cancel-1] == uin :
                if(input(f"Cancel seat {seat_to_cancel} ? (y/n) ") == "y"):
                    seat_list[seat_to_cancel-1] = 0 

            elif seat_list[seat_to_cancel-1] != uin :
                print("The choosen seat in not your seat")
            else :
                print("Invalid input")

    if seat_booked != True:
        print("No seats booked in reserved")


    if len(waiting_seat_list) != 0:
        for i in range(TOTAL_SEATS):
            if seat_list[i] == 0 :
                seat_list[i] = waiting_seat_list[0][0]
                if waiting_seat_list[0][1] != 1:
                    waiting_seat_list[0][1] -= 1
                else :
                    del waiting_seat_list[0]


    waiting_seat_booked = False
    for i in range(len(waiting_seat_list)):
        if waiting_seat_list[i] == uin :
            print(f"Waiting list number {i+1}")
            waiting_seat_booked = True
            break

    if waiting_seat_booked == True:
        while(input("Cancel seats in waiting list ? (y/n) " == "y")):
            k = int(input("How many seats to cancel ? "))  
            if k > 0 and k <= waiting_seat_list[i][1] :
                waiting_seat_list[i][1] -= k 
            else :
                print("Invalid input")         
    
    else :
        print("You have no seats booked under this UIN")

    user_choice(uin,name)

    
def seat_status(uin, name):

    print("Name :",name)
    print("UIN :",uin)

    print("Seats booked : ")
    seat_booked = False 
    for i in range(TOTAL_SEATS):
        if seat_list[i] == uin :
            print(f"Seat number {i+1}")
            seat_booked = True

    if seat_booked == False:
        print("No seats booked in reserved")

    print("Seats in waiting list : ")
    waiting_seat_booked = False
    for i in range(len(waiting_seat_list)):
        if waiting_seat_list[i][0] == uin :
            print(f"Waiting list number {i+1}, {waiting_seat_list[i][1]} seats")
            waiting_seat_booked = True

    if waiting_seat_booked == False :
        print("No seats in waiting list")

    user_choice(uin, name)

if __name__ == "__main__":
    seat_list = [0]*TOTAL_SEATS
    waiting_seat_list = []
    name_list = []

    check_user()