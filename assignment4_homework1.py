a=input("Enter the file name: ")

try:
    file=open(a,'r')
    print("Reading file contents: \n")
    a = file.read()
    print(a)
    file.close()
except:
    print("ERROR: The file",a,"was not found")