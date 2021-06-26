f = open("file1.txt","r")
s = f.read()
f.close()

f1 = open("file2.txt","w")
f1.write(s)
f1.close()

f2 = open("file2.txt","r")
print(f2.read())
f2.close()
