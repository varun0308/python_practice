import json

x = '{ "1" :"John", "age":30, "city":"New York"}'
# x = '{ 1 :"John", "age":30, "city":"New York"}'   This type doesn't work for to be known reasons 
t = {"12345" : "Varun","98765" : "Kumar"}

y = json.loads(x)     # y is of type dict

y.update(t)

z = json.dumps(y)       # z is string

print(z)
print(type(z))

