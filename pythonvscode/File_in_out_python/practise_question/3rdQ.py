with open("sample.txt",'r') as f:
    data=f.read()
    print(data)
    
    # num=""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(num)
    #         num=""
    #     else:
    #         num=num+data[i]  
    nums=data.split(",")
    print(nums) 
    cnt=0
    for val in nums:
        if(int(val)%2==0):
            cnt+=1
print(cnt)
     