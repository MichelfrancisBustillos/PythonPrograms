
fileName = input("Enter file name: ")
try:
    fhand = open(fileName)
except:
    print('File cannot be opened:', fileName)
    exit()

for line in fhand:
    print (line)
#searchTerm = input("Enter term to search in file: ")
#count = 0
#for line in fhand:
#    if searchTerm in line:
#        count = count + 1
#print ('There where', count, 'instances of', searchTerm, 'in', fileName)
fhand.close()
