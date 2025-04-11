# লিস্ট কম্প্রিহেনশন লিস্ট কম্প্রিহেনশন হলো একটা 
# এক লাইনের for লুপ যা সফলতার সাথে একটা লিস্ট ডেটা স্ট্রাকচার 
# তৈরি করে।

mylist=[i**2 for i in range(20) if i%2==0]
print(mylist)
print()

# সেট কমপ্রিহেনশন #
a_list=["Maateen",'Khan','Maksudur','a','b','c']
print(a_list)
my_set={i for i in a_list if len(i)>1}
my_set1={i for i in a_list if len(i)==1}
print(my_set)
print(my_set1)
print()

#ডিকশনারি কমপ্রিহেনশন 
a_list=['name','country','career']
b_list=['Maateen','Bangladesh','Teletalk']
my_dict={i:j for i,j in zip(a_list,b_list)}
print(my_dict)
'''এখানে zip() ফাংশন ব্যবহার করে আমরা দুটি লিস্টকে সমান্তরালভাবে ইটারেট করেছি। 
zip() ফাংশনের বিষয়ে একটু জানাশোনা থাকা দরকার আমাদের। এই ফাংশন একাধিক ইটারেবল
প্যারামিটার হিসেবে নেয়, কিন্তু রিটার্ন করে কেবলমাত্র একটি ইটারেটর (টাপলের), যেখানে n-তম 
টাপলে প্যারামিটার হিসেবে নেওয়া প্রতিটি ইটারেবলের n-তম আইটেম থাকে। একটি 
উদাহরণ দিলে বিষয়টি আরও পরিষ্কার হবে।'''

a=[i for i in range(11)]
print(a)
b=[i for i in range(11,21)]
print(b)
c=zip(a,b)
print(list(c))
print()

#  কীভাবে ডিকশনারি কম্প্রিহেনশন কাজে লাগানো যায় -
my_dict={
    'career':'Teletalk',
    'country':'Bangladesh',
    'Name':'Maateen'
}
print(my_dict)
new_dict={key:value for value,key in my_dict.items()}
print(new_dict)
