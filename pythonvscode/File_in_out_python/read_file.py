#File I/O in Python
#python can be used to perform on a file.(read &write data)
#Types of all files
# 1.Text Files 2.Binary file
f=open(r"E:\pythonvscode\File_in_out_python\demo.txt","rt")
data=f.read()
# data=f.read(10)  #reads a entire a file
print(data)
line1=f.readline() #reads one line at a time
line2=f.readline()
line3=f.readline()
print(line1)
print(line2)
print(line3)
# print(type(data))
f.close()