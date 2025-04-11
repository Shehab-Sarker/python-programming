#Problem 06
#ইউজার একটা পূর্ণসংখ্যা ইনপুট দেবে, এই ইনপুট হল তার লাঞ্চ বিল। এবার 
# এটাকে আমাদের দেশের হিসেব অনুযায়ী কত টাকার কয়টা 
# নোট দিয়ে বিল দেয়া যাবে সেটা বের করতে হবে।   

a=int(input("Please input your lanch bill:"))
b=a
temp=a//1000
print(f"{temp} ti 1000 taka note(s).")
if temp>0:
    a=a%1000
    b=a
else:
    a=b
temp=a//500
print(f"{temp} ti 500 takar note(s)")
if temp>0:
    a=a%500
    b=a
else:
    a=b
temp=a//200
print(f"{temp} ti 200 takar note(s).")
if temp>0:
    a=a%200
    b=a
else:
    a=b
temp=a//100
print(f"{temp} ti 100 takar note(s).")
if temp>0:
    a=a%100
    b=a
else:
    a=b
temp=a//50
print(f"{temp} ti 50 taka note(s).")
if temp>0:
    a=a%50
    b=a
else:
    a=b
temp=a//20
print(f"{temp} ti 20 takar note(s)")
if temp>0:
    a=a%20
    b=a
else:
    a=b
temp=a//10
print(f"{temp} ti 10 takar note(s).")
if temp>0:
    a=a%10
    b=a
else:
    a=b
temp=a//5
print(f"{temp} ti 5 takar note(s).")
if temp>0:
    a=a%5
    b=a
else:
    a=b 
temp=a//2
print(f"{temp} ti 2 takar note(s).")
if temp>0:
    a=a%2
    b=a
else:
    a=b  
temp=a//1
print(f"{temp} ti 1 takar note(s).")
print('')

# Problem 7:
# ইউজার তার জন্মসাল ইনপুট দেবে।
# চেক করে দেখতে হবে সেটা লিপ-ইয়ার কিনা
year=int(input("Please,Enter your Birth year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print("Leap Year.")
else:
    print("Not Leap year")
