#loop
'''লুপ মানে ফাঁস। ফাঁস আমরা সবাই চিনি। এটা নিয়ে রাজনীতি করার কিছু নাই। 
কিন্তু প্রোগ্রামিংয়ের লুপ নিয়ে বলার আছে অনেক কিছুই। এই লুপ মানে হল বারবার।
যখন একই কাজ বারবার করার দরকার পড়ে তখন লুপ ব্যবহার করতে হয়। লুপকে
কন্ডিশনাল লজিকের ভিতরেই ফালানো যায়। কারণ লুপে কন্ডিশনের উপর ভিত্তি করেই 
একই কাজ বারবার করা হয়।'''
# n=1
# while n<=10:
#     print(n)
#     n+=1
n=10
for i in range(0,n+1):
    print(i)
print('')

#1+2+3+4+…+100 = ? বের করা। while
# লুপ ব্যবহার করে আমরা এখন এটার সলিউশন করব।
n=1
temp=0
while n<=100:
    temp+=n
    n+=1
print(temp)
# n=100
# temp=n*(n+1)
# temp=temp/2
# print(temp)
print('')

#for লুপ দিয়ে আমরা এসব সিকুয়েন্সিয়াল আইটেমকে ইটারেট 
# করতে পারি। ইটারেট করা মানে হল আইটেম বাই আইটেম রিড করতে পারা।
# যাকে ইটারেট করা যায় তাকে ইটারেটর (Iterator) অবজেক্ট বলে।
# লিস্ট, টাপল, সেট, ডিকশনারি সবাইকেই ইটারেট করা যায়।
a=['onion','potato','ginger','cucumber']
print(type(a))
print(a)
for item in a:
    print(item)
    # print(item,end=' ')
print('')

a={
    'name':'Shehab Sarker',
    'age':25,
    'city':'Dhaka',
    'nickname':'maateen',
    'email':'maateen@outlook.com',
    'phone': '1711223344'
}
print(type(a))
print(a)
for item in a:
    print(item)
    
print('')

#pass স্টেটমেন্ট হল একটা নাল 
# (null) অপারেশন। এটা যখন এক্সিকিউট হয় 
# তখন আসলে কিছুই ঘটে না। প্রশ্ন হতে পারে তাহলে 
# এটা কোন কাজে লাগে। লাগে, লাগে! লাগালেই লাগে। 
   
for number in range(1,11):
    if  number == 5:
        pass
    print(number)
print('')

#পাইথনে লুপের সাথে আমরা চাইলে else ব্যবহার করতে পারি। while 
# লুপে else স্টেটমেন্ট ইউজ করলে, যখন while লুপের এক্সপ্রেশনটা মিথ্যা 
# হবে তখনই else ব্লক এক্সিকিউট হওয়া শুরু হবে 

n=1
while n<=10:
    print(n)
    n+=1
else:
    print("The loop is Over.")
print('')

# print("Infiniti Loop:")
# i=1
# while i>0:
#     i+=1
#     print(i)

