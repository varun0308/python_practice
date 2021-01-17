number = input("Number")

#Dictionary
mapping={
    "1":"One",
    "2":"Two",
    "3":"Three"
}

output=""
for x in number:
   output += mapping.get(x, "R") +" "

print(output)
