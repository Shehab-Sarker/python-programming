# Problem 01:
'''ইউজার যেকোনো একটা পূর্ণসংখ্যা ইনপুট দেবে। আর ওই পূর্ণসংখ্যার
নামতা আউটপুট হিসেবে দেখাতে হবে।'''
num=int(input("Please, input your number: "))
# i=1
# while i<=10:
#     print(f"{num} * {i} = {num*i}")
#     i+=1
# print('')
for i in range(1,11):
    # print(f"{num} * {i} = {num*i}")    
    print(num,"*",i,"=",(num*i))
print('')  

# problem 02;  
'''১ থেকে ১০০ পর্যন্ত যেসব সংখ্যা ৩ দ্বারা নিঃশেষে বিভাজ্য
কিন্তু ৫ দ্বারা নয়, তাদের লিস্ট আউটপুট হিসেবে দেখাতে হবে।'''
my_list=[]
for i in range(1, 101):
    if i%3==0 and i%5!=0:
        my_list.append(i)      
print(my_list)
print('')

# problem 03:
'''ধরা যাক, বিভিন্ন সংখ্যার একটি তালিকা রয়েছে। তালিকাটা নিচের মত 
13, 34, 19, 28, 46, 61, 73, 49, 1, 31, 4, 7, 91, 58, 52, 82,
70, 43, 88, 55, 97, 16, 22, 25, 79, 85, 40, 64, 94, 67, 37
এই তালিকা থেকে ৫০-এর চেয়ে ছোট সংখ্যাগুলোকে নিয়ে একটি লিস্ট
বানিয়ে আউটপুট হিসেবে দেখাতে হবে।'''

mylist=[13, 34, 19, 28, 46, 61, 73, 49, 1, 31, 4,
        7, 91, 58, 52, 82, 70, 43, 88, 55, 97, 16,
        22, 25, 79, 85, 40, 64, 94, 67, 37]
mylist1=[]
for i in mylist:
    if i<50:
        mylist1.append(i)
print(mylist1)  
print('')

#Problem 4:
'''নিচের তালিকাটি লক্ষ্য করা যাক -
40, 45, 33, 34, 8, 38, 28, 22, 1, 7, 49, 41, 14, 5, 22, 39, 15, 19,
36, 37, 43, 2, 5, 42, 46, 48, 49, 12, 48, 37, 8, 20, 30, 20, 4, 37, 
27, 29, 7, 44, 15, 32, 35, 10, 28, 18, 2, 15, 36, 38
এই তালিকা থেকে সকল ডুপ্লিকেট (duplicate) ভ্যালু রিমুভ করতে হবে।'''   

mylist2=[40, 45, 33, 34, 8, 38, 28, 22, 1, 7, 49, 41, 14, 5, 22, 39, 15, 19,
        36, 37, 43, 2, 5, 42, 46, 48, 49, 12, 48, 37, 8, 20, 30, 20, 4, 37, 
        27, 29, 7, 44, 15, 32, 35, 10, 28, 18, 2, 15, 36, 38]
mylist3=[]
for i in mylist2:
    if i not in mylist3:
        mylist3.append(i)
print(mylist3)    

# problem-5:
'''ইউজার একটা পূর্ণসংখ্যা ইনপুট দেবে। সেটির ওপর ভিত্তি করে
আমরা *এর স্কয়ার ডিজাইন করব। অর্থাৎ ইউজার যদি 5 ইনপুট 
দেয় তাহলে নিচের মতো একটা স্কয়ার ডিজাইন করব।
*****
*****
*****
*****
*****'''   
num=int(input("Please, Enter the input for * square design:"))
for i in range (0,num):
    for j in range(0,num):
        print("*",end="")
    print(' ') 
print()

# Problem 06
'''ইউজার একটি শব্দ ইনপুট দেবে। আমাদের প্রোগ্রাম দেখবে সেটি একটি প্যালিনড্রোম
(Palindrome) কি না! প্যালিনড্রোম হলো কোনো শব্দ, সংখ্যা বা সিক্যুয়েন্স যাদের 
ওলটালেও ওই এক জিনিসই থাকে। যেমন : 707 কে ওলটালেও 707 ই থাকে। 
আবার Madam-কে ওলটালে Madam ই থাকে।'''
print("Please input your word:")
word=input()
word=word.casefold()
print(word)
reversed_word=word[::-1]
print(reversed_word)

if word==reversed_word:
    print("Great! It is a pallindrome.")
else:
    print("LOL! It is not a pallindrome.")   
print('')

# Problem 07
'''এখন আমরা অনন্ত জলিলের খোঁজ দ্য সার্চ-এর প্রবলেম সলভ করব। ধরা যাক, 
ছোট থেকে বড় সাজানো বিভিন্ন সংখ্যার একটা তালিকা আছে। তালিকাটা নিচের মতো—
1, 3, 5, 7, 11, 13, 15, 17, 20, 26, 31, 44, 54, 56, 65, 77, 94, 100
এই তালিকা থেকে ইউজারের ইনপুট দেওয়া নির্দিষ্ট একটি সংখ্যা 
খোঁজ দ্য সার্চ করে বের করতে হবে। এ আর কঠিন কী!'''
mylist4=[1, 3, 5, 7, 11, 13, 15, 17, 20, 26, 31, 44, 54, 56, 65, 77, 94, 100]

num=int(input("Input the number: "))
first=0
last=len(mylist4)-1
found=False
cycle=0

while first<=last and not found:
    midpoint=(first+last)//2
    if mylist4[midpoint]==num:
        found=True
    else:
        if num < mylist4[midpoint]:
            last=midpoint-1
        else:
            first=midpoint+1
    cycle+=1
    
print("Found after",cycle,"cycle.")
print()

# Problem:
'''(২) ইউজার একটা পূর্ণসংখ্যা ইনপুট দেবে। সেটির ওপর ভিত্তি করে আমরা *এর ত্রিভুজ ডিজাইন করব।
অর্থাৎ ইউজার যদি 5 ইনপুট দেয় তাহলে নিচের মত একটা ত্রিভুজ ডিজাইন করব।'''
num=int(input("Please, Input the number: "))
for i in range(0,num):
    for j in range(0,i+1):
        print("*",end='')
    print()
print()

# Problem
'''A = {1, 2, 3, 4, 5} ও B = {5, 6, 7, 8} দুটি সেট। union() ও intersection() ফাংশন 
(আসলে মেথড) ব্যবহার না করে তাদের ইউনিয়ন ও ইন্টারসেকশন সেট C বের করতে হবে।'''
A={1,2,3,4,5}
B={5,6,7,8}
C=set()
D=set()
for i in A:
    if i in B:
        C.add(i)
    if i not in D and i not in B:
        D.add(i)
        
# for i in B:
#     if i not in D:
#         D.add(i)
D.update(B)
print(C)
print(D)
print()

#(৩) ১ থেকে ১০০-এর ভিতর যেসকল সংখ্যা রয়েছে,
# সেখান থেকে দৈবচয়নের মাধ্যমে বাছাই করে ন্যূনতম ত্রিশ সংখ্যার 
# একটা লিস্ট তৈরি করতে হবে। এই লিস্টে একই সংখ্যা একাধিকবার 
# থাকতে পারবে না। (এখন পর্যন্ত অর্জিত জ্ঞান দিয়ে সলভ করতে না পারলে, 
# পুরো বই শেষ করে আবার চেষ্টা করতে হবে।)
import random
ran_number=[]
for i in range(30):
    num=random.randint(1,100)
    ran_number.append(num)
print(ran_number)