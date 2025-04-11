'''ইউজার এক লাইনে তিনটা পূর্ণসংখ্যা ইনপুট দেবে (যেমন: 23 10 96)। 
সবচেয়ে বড় সংখ্যাটি বের করতে হবে।'''
# print("Please enter your three integers:")
a,b,c=map(int,input("Please enter your three integers:").split())

def bigg_num(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z
print("Biggest number are:",bigg_num(a,b,c)) 

#Problem 02:
#ছোটবেলায় স্কুলে আমরা গ.সা.গু বা গরিষ্ঠ সাধারণ গুণনীয়কের অনেক সমস্যা
# সমাধান করেছি। ইংরেজিতে একে বলা হয়, GCD বা Greatest Common Divisor। 
# দুটি সংখ্যার GCD বের করার জন্য একটি ফাংশন লিখতে হবে
a,b=map(int,input("Please Enter your Two number for GCD: ").split())
def gcd(a,b):
    x=a
    y=b
    while y!=0:
        r=x%y
        x=y
        y=r
    return x
print('Greatest Common Divisor is : ',gcd(a,b))
print('')
'''প্রব্লেম-৩: #
গ.সা.গু তো হয়ে গেল। ল.সা.গু বা লঘিষ্ঠ সাধারণ গুণিতকই বা বাদ থাকবে কেন? 
ইংরেজিতে একে বলা হয় LCM বা Least Common Multiple।
দুটি সংখ্যার LCM বের করার জন্য একটি ফাংশন লিখতে হবে।'''
a,b=map(int,input("Please Enter your Two number for lCM: ").split())
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def LCM(a,b):
    return (a*b)//gcd(a,b)
print('Least Common Multiple is :',LCM(a,b))
print('')

# Problem 04
'''ইউজার একটি পূর্ণসংখ্যা ইনপুট দেবে। আমাদের বলতে হবে
সেটি মৌলিক (Prime) সংখ্যা, নাকি যৌগিক (Composite) সংখ্যা।'''
num=int(input("Please, Input your number:"))
for i in range(2,num//2):
    if num%i==0:
        temp=0
        break
    else:
        temp=1
if temp:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number.")
    
# or
def is_prime(num):
    if num<=1:
        raise ValueError("The number must be greater than 1.")
    elif num<=3:
        return True
    elif (num%2==0) or (num%3==0):
        return False
    else:
        i=5
        while (i*i)<=num:
            if(num%i)==0 or (num%i+2)==0:
                return False 
            i+=6
        return True
if is_prime(num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is a composite number.')
    
        