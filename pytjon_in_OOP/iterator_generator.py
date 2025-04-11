'''__next__() মেথড দিয়ে আমরা একটা ইটারেটরের পরবর্তী
এলিমেন্ট বা আইটেমকে অ্যাক্সেস করতে পারি। সবগুলো আইটেম অ্যাক্সেস
করতে করতে যখন আর কোন আইটেম বাকি থাকে না তখন
পাইথন StopIteration এরর থ্রো করে।'''  
x=iter([1,2,3])
print(x)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print()
'''range() ফাংশনের মত কাজ করবে, তবে রিভার্সলি। মানে range(5) মানে তো
0, 1, 2, 3, 4। কিন্তু আমাদের তৈরি ইটারেটর ক্লাস এটাকে 5, 4, 3, 2, 1, 0
এরকম কিছু একটা বানাবে। তো চেষ্টা করা যাক।'''
class revrange:
    def __init__(self,n):
        self.n=n
        self.i=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>=0:
            if self.i==self.n:
                self.n=self.n-1
                return self.i
            else:
                self.i=self.n
                self.n=self.n-1
                return self.i
        else:
            raise StopIteration
        
for temp in revrange(5):
    print(temp)
print()
'''জেনারেটর #
জেনারেটর একটা ফাংশন। এই ফাংশনের কাজ হল yield স্টেটমেন্ট
ব্যবহার করে সিকুয়েন্স পয়দা করা।
এইদিক থেকে জেনারেটরও এক ধরনের ইটারেটর।'''
def revrange(n):
    while n>=0:
        yield n
        n-=1
        
for temp in revrange(5):
    print(temp)