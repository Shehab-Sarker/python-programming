#Read and writng by r+ ,its read and overwriting existing data
# f=open('rdemo.txt','r+')
# f.write("ami pari na kno")
# print(f.read())
# f.close()


#read and writing by w+
# f=open('rdemo.txt','w+')
# f.write("ami pari na kno\n")
# print(f.read())
# f.write("where are you from\n")
# f.close()

#Read and Writing by a+
f=open('rdemo.txt','a+')
print(f.read())
f.write("ami pari na kno\n")
f.close()