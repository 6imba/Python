import time
 
print(time)
print(time.time())
print(time.gmtime)
print(time.gmtime(0))

for i in range(4):
    # using sleep() to hault execution
    time.sleep(1)
    print(i)