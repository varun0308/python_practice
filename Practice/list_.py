n = int(input())

list_ = []
for i in range(n):
    ele = input().split()
    list_.append(ele)

list_.pop(3)
print(list_)


list__ = []
list__.append(input().split())
list_.remove("h") 

print(list__)