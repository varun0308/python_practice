""""
1 male and 1 female rabbits 
Mate at 1 month
1 month gestation period
Gives 1 pair of rabbit each time
How many female rabbits at end of 1 year
And they don't die

"""
def calculate(month_count):
    if month_count <= 1 :
        return 1
    else :
        return calculate(month_count-1) + calculate(month_count-2)
        
count_male = count_female = 1
month_count = int(input())


print(calculate(month_count))