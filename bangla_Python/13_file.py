#পাইথনে ফাইল ওপেন করার জন্য open()
# ফাংশনটা ব্যবহার করব আমরা।
my_file=open('test.txt','r')
content=my_file.read()
print(content)
my_file.close()
print()
my_file=open('test.txt','w')
my_file.write('I am Shehab Sarker.')
my_file.close()

my_file=open('test.txt','a')
my_file.write('I am from Bangladesh.')
my_file.close()
print()

my_file=open('test.txt','r')
content=my_file.read(5)
print(content)
content=my_file.read()
print(content)
position=my_file.tell()
print(position)
my_file.seek(0,0)
content=my_file.read()
print(content)
my_file.close()
print()

with open('test.txt','r') as my_file:
    content=my_file.read()
    print(content)
   