# type(a)
# <class'str>
# type(b)
# <class'str'>
# print("Bangla is my \"motherland\",I love her very much ")
# print('\n')
# print('\t',"Okay, I am here")
# print('\\')

a="bangla"
b="desh"
c=a+b
print(c)
print(a[1:4])
print(a[:])
print(a)
print(a[2:])
print(a[:3])
print("")

number=436.15757823658945
print(number)
print("%0.2f"%number)
print("%0.3f"%number)
print("%0.4f"%number)

print("")

#String_Formating
# a=input()
# b=input()

# print("My favorite languages are : ",a, "and",b)
# print("My favourite language are : %s and %s"%(a,b))
# print("")

d="love"
X="-".join((a,b,d))
print(X)
print("")

#বড় করি, ছোট করি ,capitalize() ফাংশন ব্যবহার করব। এই ফাংশন কোন স্ট্রিংয়ের প্রথম ক্যারেক্টারটাকে বড় হাতের বানায়।
print(a.capitalize())

#যদি সবগুলো ক্যারেক্টারকেই বড় হাতের করতে চাইতাম তবে upper() ফাংশন ব্যবহার করতে হত।
print(a.upper())

#বাক্যের প্রতিটা শব্দের প্রথম অক্ষরকে বড় হাতের করতে চাই তবে আমাদেরকে title() ফাংশন ব্যবহার করতে হবে।
print("bangaldesh is my motherland. i just love her.".title())

#একটা স্ট্রিংয়ের সবগুলো ক্যারেক্টারকে ছোট হাতের করার জন্য lower() , casefold() ফাংশন ব্যবহার করা হয়।
y="BANGLADESH"
print(c.lower())
print('')

#বড় হাতেরকে ছোট হাতের করতে হবে আর ছোট হাতেরকে বড় হাতের করতে হবে তখন আমরা swapcase() ফাংশন ব্যবহার করব।
print(y.swapcase())

#‘bangla’ তে a কিন্তু দুইবার আছে। পাইথন দিয়ে কিভাবে এটা হিসাব করা যায়? খুবই সহজ। এইজন্য আমরা count() ফাংশন ব্যবহার করব।
print(a.count('a'))
sentence="How can clam cram in a clean cream can?"
print(sentence.count("c"))
print(sentence.count("c",15))
print(sentence.count("c",5,9))
# বাক্যে কোন কোন ইনডেক্সে c রয়েছে তা কিভাবে খুঁজে বের করব? এইজন্য আমরা find() ফাংশন ব্যবহার করব।
print(sentence.find('c'))
print('')

#replace() ,strip() ফাংশন ব্যবহার করে আমরা সহজেই তা করতে পারি। ফাংশনটার ভিতরে প্রথমে যে ক্যারেক্টারটাকে রিপ্লেস করব সেটাকে দেব, তারপরে যাকে দিয়ে রিপ্লেস করব তাকে দেব। নিচের প্রোগ্রামটা দেখলে সব পরিষ্কার হয়ে যাবে:
print(sentence.replace("c","d"))
print(sentence.replace("c",""))
print(sentence.strip("H"))
# হোয়াইটস্পেসগুলোর উপর ভিত্তি করে split() ফাংশনের dara স্ট্রিংটাকে ভাগ করব।
print(sentence.split(" ")) 



