'''ফাংশন তৈরি ও কল করা #
পাইথনে ফাংশন তৈরির বা লেখার নির্দিষ্ট নিয়ম কানুন আছে।
ফাংশন ব্লক def কি-ওয়ার্ড দিয়ে শুরু হবে। def এর পর একটা 
স্পেস দিয়ে ফাংশনের নাম থাকবে। ফাংশনের নাম ভ্যারিয়েবলের নামের 
মতই হতে পারে। তবে ফাংশনের নাম আন্ডারস্কোর _ দিয়ে শুরু করা যায়।'''
def print_my_name(myname):
    print(f"The given name is {myname}")
    
print_my_name('Shehab')

def add(a,b,c):
    return a+b+c
temp=add(1,2,3)
print(temp)
print()

'''ফাংশন প্যারামিটার বা আর্গুমেন্ট #
ফাংশনে এই যে প্যারামিটার বা আর্গুমেন্ট আমরা ব্যবহার করতেছি এদেরকে মোটামুটি চারভাগে ভাগ করতে পারি।
রিক্যুয়ার্ড আর্গুমেন্ট (Required argument)
কি-ওয়ার্ড আর্গুমেন্ট (Keyword argument)
ডিফল্ট আর্গুমেন্ট (Default argument)
ভ্যারিয়েবল লেংথ আর্গুমেন্ট (Variable-length argument)'''

# Required argument
# keyword argument
def add(a, b, c):
    return a+b+c
temp = add(b=2, c=3, a=1)
print(temp)
# default argument
def add(a,b,c=3):
    return a+b+c
print(add(1,2))
# default argument
def add(a,b,c=3):
    return a+b+c
print(add(1,2,75))
# Variable-length argument (অ্যাসটেরিস্ক * )
# non-keyword Variable-length
def add(*args):
    print(type(args))
    tmp=0
    for num in args:
        tmp+=num
    return tmp
temp=add(1,2,22,12,17,21,98)
print(temp)
'''ফাংশনের যেকোন প্যারামিটারের আগে একটা অ্যাসটেরিস্ক * চিহ্ন দিলে সেটা
আনলিমিটেড ভ্যালু হোল্ড করতে পারে। জেনে রাখা ভাল, এই প্যারামিটারটা 
একটা টাপল তৈরি করে সবগুলো ভ্যালু হোল্ড করে। পরে একটা for
লুপ চালিয়ে আমরা সবগুলো ভ্যালু অ্যাক্সেস করতে পারি। এটাকে
নন-কীওয়ার্ডেড (non-keyworded) ভ্যারিয়েবল লেংথ আর্গুমেন্ট বলা হয়।'''
#keyword variable-length
def add(**kwargs):
    print(type(kwargs))
    tmp=0
    for key in kwargs:
        tmp+=kwargs[key]
    return tmp
temp=add(a=1,b=3,c=2,d=4)
print(temp)

#Recursion
'''রিকার্সন একটা মজার জিনিস। যখন কোন ফাংশন নিজেই নিজেকে ডাকে
তখন আমরা তাকে রিকার্সন বলি। আর ঐ ফাংশনটাকে বলি রিকার্সিভ (Recursive) 
ফাংশন। নিজেকে নিজে ডাকে মানে হল নিজের ভিতরেই আবার নিজেকে কল করবে।'''
def counter(num):
    print(num)
    num+=1
    counter(num)
# counter(1)  
# Factorial problem
print("Please input your number:")
number=int(input())
temp=number

while number > 1:
    number-=1
    temp*=number
if temp==0:
    print(1)
else:
    print(temp)
# when recursion function use for factorial detemine
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
number=int(input("Please input your (factorial) number: "))
print(factorial(number))
print()

# এক লাইনের ফাংশন - ল্যাম্বডা (lambda) 
# #lambda অপারেটর ইউজ করে পাইথনে এক লাইনের 
# ফাংশন লেখা যায়। lambda এর পর স্পেস দিয়ে আর্গুমেন্ট
# দিতে হয়। তারপর কোলন : চিহ্ন দিয়ে 
# অ্যারিথমেটিক এক্সপ্রেশন দিতে হয়।
sum=lambda a,b : a+b
print(sum(10,20))
print((lambda a,b : a+b)(10,20))
def my_function(func,arg1,arg2):
    return func(arg1,arg2)
print(my_function(lambda a,b :a+b,10,20))
print() 

'''map() একটা বিল্ট-ইন ফাংশন। কিন্তু ফাংশন (বিল্ট-ইন বা ইউজার 
ডিফাইন্ড) অ্যাপ্লাই করার ক্ষেত্রে এর ব্যবহার ব্যাপক। ম্যাপ কাজ করার জন্য 
দুইটা আর্গুমেন্ট নেয় - প্রথমটা হল ফাংশন আর দ্বিতীয়টা হল ইটারেটর অবজেক্ট। 
এর কাজ হল ইটারেটর অবজেক্টের প্রতিটা আইটেমের উপর আর্গুমেন্ট
হিসাবে নেয়া ফাংশনটাকে অ্যাপ্লাই করবে।'''

mylist=[2,3,4,5,6,7]
def square(x):
    return x*x

newlist=map(square,mylist)
print(list(newlist))
print()

# ইউজার ডিফাইন্ড ফাংশনকে অ্যাপ্লাই করলাম। এবার আমরা একটু বিল্ট-ইন ফাংশন নিয়ে খেলব।
a,b=map(int ,input().split())
print(a+b)
print()

'''filter() #
অনেকটা ম্যাপ ফাংশনের মতই। তবে এর কাজ হল ফিল্টারিং করা।
সত্য-মিথ্যার উপর ভিত্তি করে ফিল্টারিং করে। ফিল্টার কাজ করার জন্য
দুইটা আর্গুমেন্ট নেয় - প্রথমটা হল ফাংশন আর দ্বিতীয়টা হল ইটারেটর অবজেক্ট। এর কাজ হল 
ইটারেটর অবজেক্টের প্রতিটা আইটেমের উপর আর্গুমেন্ট হিসাবে নেয়া ফাংশনটাকে অ্যাপ্লাই করবে।'''
mylist=[2,3,4,5,6,7]

def is_even(x):
    if (x%2)==0:
        return True
    else:
        return False
newlist=filter(is_even,mylist)
print(list(newlist))