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
    a,b,c = [int(x) for x in input("Sides ").split(" ")]      # Can use input("Sides ").input      # But will have to use int(a)....     # Because input is in str
    print(area_triangle(a,b,c))

elif int(sides) == 4:
    a,b = [int(x) for x in input("Sides ").split(" ")]
    area_rectangle(a,b)

else :
    print("Can't solve it")