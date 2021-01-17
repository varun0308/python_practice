password = input("Enter Password : ")
con_password = input("Confirm password : ")

i=1
while password != con_password and i!=4:
    print("Password did not match")
    con_password = input('Retry password : ')
    i+=1

if i==4:
    print("System locked\nToo many incorrect retries")
else:
    print('Password accepted')