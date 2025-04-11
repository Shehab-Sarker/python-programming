'''ওয়ালটন উস্তা’ ক্লাসটা, এটা দিয়ে আমরা কিন্তু লাখ
লাখ গাড়ি তৈরি করতে পারি। প্রতিটা গাড়িতেই কিন্তু ঐ চারটা 
ফাংশন থাকবে। এখন আমাদের গাড়িটার কথা ধরি। আমাদের
গাড়িটাও তো ‘ওয়ালটন উস্তা’ ক্লাস থেকে তৈরি। তাহলে 
আমাদের গাড়িটা হল ঐ ক্লাসের একটা অবজেক্ট। ঐ 
ক্লাস থেকে তৈরি সব গাড়িই এক-একটা অবজেক্ট।'''
class WaltonUsta:
    '''Our new class'''
    
    def driving(self):
        return 'run_the_car'
    
    def music(self):
        return 'run_the_music'
        
    def fuel(self):
        return 'load_the_fuel'
        
    def horn(self):
        return 'make_sound_pollution'
        
our_car=WaltonUsta()
her_car=WaltonUsta()
your_car=WaltonUsta()

'''ক্যালকুলেটরের জন্য একটা ক্লাস তৈরি করব। এই ক্লাসে যোগ, 
বিয়োগ, গুণ ও ভাগের জন্য মেথড থাকবে।'''
class Calculator:
    '''Do addition,subtraction, multiplication and division '''
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "It is impossible to divide by Zero."

my_calculator=Calculator()

temp=my_calculator.addition(12,78)
print(temp)

temp=my_calculator.subtraction(50,23)
print(temp)

temp=my_calculator.multiplication(9,19)
print(temp)

temp=my_calculator.division(43,0)
print(temp) 
print( )

'''ক্লাসের প্রথম মেথড হিসাবে __init__ ব্যবহার করতে হবে। প্রোগ্রামিংয়ের ভাষায় 
একে ক্লাস কনস্ট্রাক্টর (constructor) বলে। যখন কোন ক্লাসের নতুন ইন্সট্যান্স বা
অবজেক্ট তৈরি করি আমরা তখন পাইথন নিজ থেকেই ক্লাস কনস্ট্রাক্টরকে কল করে। 
ওহ! যখন ক্লাস কনট্রাক্টর আমরা ডিফাইন করি না তখন পাইথন নিজ 
থেকেই ক্লাস কনস্ট্রাক্টর ডিফাইন করে নেয়।''' 

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return 'It is impossible to divide by Zero.'
my_calculator=Calculator(45,3)
print(my_calculator.addition())
print(my_calculator.subtraction())
print(my_calculator.multiplication())
print(my_calculator.division())
