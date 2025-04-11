'''With Syntax
with open("demo.txt","a) as f
data=f.read()'''
with open("sdemo.txt","r") as f:
    data=f.read()
    print(data)

with open("sdemo.txt","w") as f:
    f.write("NEW COLLECTion IN MY University")