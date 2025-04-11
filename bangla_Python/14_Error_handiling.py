'''est.txt ফাইলটা না পেয়ে FileNotFoundError থ্রো করেছে পাইথন, 
তারপর প্রোগ্রামের এক্সিকিউশন বন্ধ হয়ে গেছে। ফলে 
শেষের নির্ভেজাল স্টেটমেন্টটাও এক্সিকিউট হয় নাই। 
এইরকম সমস্যার নিরসন করতেই এক্সেপশন হ্যান্ডলিং 
বা এরর হ্যান্ডলিং।
try … except #'''
try:
    with open('text.txt','r') as my_file:
        content=my_file.read()
        print(content)
except:
    print("The file does not exist")
print("Made by Shehab")

'''try...except এর ব্যাপারটা হল এরকম: নরমাল কোডগুলো try ব্লকের ভিতর থাকবে। 
আর কোন এক্সেপশন রেইজ হলে except ব্লকের কোড এক্সিকিউট হবে। কোন নির্দিষ্ট
এক্সেপশন হ্যান্ডেল করার জন্য কোড লিখতে চাইলে except এর পরে স্পেস দিয়ে
এক্সেপশনের নাম দিয়ে দিতে হয়। আবার চাইলে এক্সেপশনের থ্রো করা মেসেজ 
হোল্ড করে প্রিন্ট করে ইউজারকে দেখানোও যায়।'''

try:
    with open('text.txt','r') as my_file:
        content=my_file.read()
        print(content)
except FileNotFoundError:
    print('The file does not exist.')
print('Made by Maateen.')

try:
    my_list=[1,2,3]
    print(my_list[4])
except IndexError as e:
    print(e)
print()

'''try ব্লকের জন্য যত খুশি তত except ব্লক লেখা যায়।
তবে প্রতিটা except ব্লকে এক্সেপশনের নাম উল্লেখ করতে হবে। 
একটা নির্দিষ্ট এক্সেপশন রেইজ হলেই কেবল ঐ নির্দিষ্ট 
except ব্লক এক্সিকিউট হবে।'''
try:
    my_file = open('test.txt')
    content = my_file.read()
    i = int(content.strip())

except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))

except ValueError:
    print("No valid integer in line.")

except:
    print("Unexpected error!")