file = open("data.txt" , "a")
file.write("\nThis should be line 3")
file.close()
# 'r' open for reading (default)
# 'w' open for writing, clearing the file first
# 'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending to the end of the file if it exists