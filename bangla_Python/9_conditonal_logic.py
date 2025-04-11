"""পাইথনে আমরা তিনটা কন্ডিশনাল স্টেটমেন্ট পাব (লুপকে হিসাবের বাহিরে রাখছি আপাতত)। 
প্রতিটার ভিন্ন ভিন্ন মানে ও কাজ আছে। এক নজরে দেখে নেয়া যাক:
if: যদি এটা সত্য হয়, তবে ওটা কর। elif: যদি if এর কন্ডিশন সত্য না হয়ে এটা সত্য হয়, তবে ওটা কর।
elif সবসময় if এর পরে আসবে। আর কেবলমাত্র if এর কন্ডিশন সত্য না হলেই elif এর কন্ডিশন এক্সিকিউট হবার সুযোগ পাবে।
else: যদি কোনটিই সত্য না হয়, তবে ওটা কর। elseও সবসময় if আর elif এর পরে আসবে (আসলে সবার শেষে)"""
a=int(input("Enter your number:"))
if a==10:
    print(f'{a} is equal 10.')
elif a<10:
    print(f"{a} is less than 10.")
else:
    print(f"{a} is greater than 10.")   
print('')

#যে পাইথনে সব নন-জিরো (non-zero) আর নন-নাল (non-null, অর্থাৎ not None) ভ্যালু হচ্ছে সত্য (True)। 
# অন্যদিকে জিরো (zero) আর নাল (null, অর্থাৎ None) ভ্যালু হচ্ছে মিথ্যা (False)।   
b=5
if b:
    print(True)
else:
    print(False) 

b=0
if b:
    print(True)
else:
    print(False)  
print('')    
    
#  is অপারেটর চেক করে যে দুটি ভেরিয়েবল একই অবজেক্টকে পয়েন্ট করছে কি না। 
# মূলত এটা আইডেন্টিটি কমপ্যারিজনে ব্যবহৃত হয়। অন্যদিকে, == (ডাবল ইক্যুয়েশন)
# অপারেটর চেক করে দেখে দুটি ভেরিয়েবল যে ভ্যালু বা অবজেক্টকে পয়েন্ট করছে তারা সমান কি না।
a=[1,2,3,4,5,6]
b=a
if b is a:
    print(True)
else:
    print(False)

b=a[:]
print(a[:3])
print(a[2:])
print(a[:])
print(b)
if b is a:
    print(True)
else:
    print(False)
print('')

 #Problem Solving
"""ইউজার একটা পূর্ণসংখ্যা ইনপুট দেবে। সংখ্যাটি ৩ ও ৫ দ্বারা
নিঃশেষে বিভাজ্য হলে আউটপুট হবে Yes আর না হলে আউটপুট হবে No।"""    
num=int(input("Please input an integer: "))
if num%3==0 and num%5==0:
    print("Yes")
else:
    print("NO")  
print('')

#Problem 2:
'''ইউজার একটা সংখ্যা ইনপুট দেবে। সংখ্যাটি ধনাত্মক হলে
আউটপুট হবে Positive, ঋণাত্মক হলে আউটপুট হবে Negative
আর জিরো হলে আউটপুট Zero হবে।'''
num=float(input("Please, input the number:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negetive")
else:
    print("Zero")    
print('') 

#Problem-3
"""ইউজার একটি পূর্ণসংখ্যা ইনপুট দেবে। সংখ্যাটি জোড় হলে
আউটপুট হবে Even আর বিজোড় হলে আউটপুট Odd হবে।"""  
num=int(input("Please,Enter the input the number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")  
print('')

#Problem 4:
#ইউজার একটি ক্যারেক্টার (আলফাবেট) ইনপুট দেবে।
# ক্যারেক্টারটা ছোট হাতের অক্ষর হলে আউটপুট হবে 
# Lower Case আর বড় হাতের অক্ষর হলে হবে Upper Case। 
# যদি ক্যারেক্টারটা আলফাবেটের মধ্যে না পড়ে, তবে আউটপুট Nothing হবে। 
char=input("please,Enter the Character(Alphabat) input:")   
if char>='a' and char<='z':
    print("Lower Case")
elif char>='A' and char<="Z":
    print("Upper Case")
else:
    print("Nothing") 
    
"""এখানে আমরা ASCII ভ্যালু হিসাব করে সিদ্ধান্ত নিয়েছি। প্রতিটি ক্যারেক্টারের
নির্দিষ্ট ASCII ভ্যালু রয়েছে। যেমন : A-এর 65, a-এর 97। a-z-এর ASCII 
ভ্যালু 97-122 আর A-Z-এর ASCII ভ্যালু 65-90। তাই আমরা এই দুটি রেঞ্জের মধ্যে হিসাব করেছি।
ASCII নিয়ে আরও জানতে আমরা এটা দেখতে পারি : http://www.asciitable.com/"""    
print('')    

#Problem 5:
'''ইউজার একটি ক্যারেক্টার (আলফাবেট) ইনপুট দেবে। ক্যারেক্টারটা ভাওয়েল (Vowel) হলে
আউটপুট হবে Vowel আর কনসোনেন্ট (Consonant) হলে হবে Consonant; যদি ক্যারেক্টারটা
আলফাবেটের মধ্যে না পড়ে, তবে আউটপুট হবে Nothing.'''
print("Please, input the character: ")
character=input()
if (character>='a'and character<='z') or (character>='A'and character<='Z'):
    if character in 'aeiouAEIOU':
        print("Vowel");
    else:
        print('Consonant')
else:
    print('Nothing') 
print('')

    
      