# non-default argument follows default argument always

import time

# default args should be after required args
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(10) # no start given then also it's okay
count(30, 15)