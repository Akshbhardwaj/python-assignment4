w=input("Enter text to write to file: ")
file=open('output.txt','w')
file_write=file.write(w)
file.close()
print("Data successfully writen to output.txt")


a=input("Enter additional text to append: ")
file=open('output.txt','a')
file_append=file.write(a)
file.close()


file=open('output.txt','r')
file_read=file.read()
print("Final contents of output.txt \n",file_read)
file.close()