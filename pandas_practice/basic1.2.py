import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)
print(myvar)
# Cannot do print(myvar[2]) when there are more than 1 columns
# To print the specific row, use loc() (refer basic3_rowcol) 

# Cannot do it as print(myvar, index)
# index is not an attribute of print, but of pandas 
print(pandas.DataFrame(mydataset,index = [1,2,3]))

