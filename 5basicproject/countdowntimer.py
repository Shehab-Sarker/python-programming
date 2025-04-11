import time

def counttime(usertime):
    while usertime:
        mins,sec=divmod(usertime, 60)
        print('{:02d} : {:02d}'.format(mins,sec))
        time.sleep(1)
        usertime=usertime-1
    print(u"Time is Finished")
     
    
usertime=int(input("Enter Second: "))
counttime(usertime)    