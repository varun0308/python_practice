# defining a function for area of triangle
def area_triangle(a,b,c):
    s=(a+b+c)/2
    area= (s*(s-a)*(s-b)*(s-c))**0.5
    return area
# defining a function for area of rectangle
def area_rectangle(a, b):
    area = a*b
    print(area)

# Asking the user for input
sides = input("Enter number of sides ")

if int(sides) == 3:
    a=int(input("Sides "))      # Can use input("Sides ").input
    b=int(input("Sides "))      # But will have to use int(a)....
    c= int(input("Sides "))     # Because input is in str
    print(area_triangle(a,b,c))

elif int(sides) == 4:
    a =int(input('Sides '))
    b =int(input('Sides '))
    area_rectangle(a,b)

else :
    print("Can't solve it")