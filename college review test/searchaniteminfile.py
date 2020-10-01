fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened: ", fname)
    quit()
search = input("Enter the character you want to search: ")
count = 0
for line in fhand:
    if line==search:
        count = count + 1
print(search, " appears ",count , "times" )
