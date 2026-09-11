# import math

# # print(math.gcd(12,18))
# print(math.lcm(4,6))
# print(math.log(2))
# print(math.log2(8))
# print(math.log10(1000))
# print(math.log(2,4))

# print(math.degrees(math.pi/4))
# print(math.radians(180))
# print(math.sin(math.radians(30)))
# print(math.cos(math.radians(30)))
# print(math.tan(math.radians(45)))

# print(math.hypot(2,3))

# print(math.dist([1,2],[4,6]))
# print(math.fabs(-10))
# print(math.fmod(10,3))
# print(math.fmod(10,5))

# random modulus everytime it generates 0to1 num only it changes values everytime when you run in random module only we have random fun
# import random


# print(random.random())   # prints a random float between 0 and 1
# print(random.randint(1,10))
# print(random.randrange(10,100))
# l=["mango","banana","kiwi","apple"]
# print(random.choices(l,k=4))
# import random

# l=[10,20,40,50,60]
# random.shuffle(l)
# print(l)
# print(random.uniform(10,20))
# l=[10,20,30,40,50,60,70]
# print(random.sample(l,k=3))
# random.seed(10)
# print(random.randrange(1,180))

# time module by using we can get function time.time/
# import time 
# print(time.time())
# print(time.ctime())
# t=time.localtime()
# print(t.tm_year)
# print(time.gmtime())
# print(time.strftime('%d-%m-%y',time.localtime()))
# print("hello")
# time.sleep(10)
# print("bye")
# starttime=time.time()
# for i in range(10000000):
#     pass
# endtime=time.time()
# print(f"execution time is: {endtime-starttime}")

# re (regular expressions)
# import re
# info="rudra contact number is 90876956789"

# result=re.findall(r'\d+',info)
# print(result)

# import os

# print(os.getcwd)
# os.chdir(r"C:\Users\viswa\OneDrive\Desktop\Pyhton>")
# os.mkdir("practice")
# os.listdir(r"C:\Users\viswa\OneDrive\Desktop\Pyhton>")
# os.rmdir()
# os.remove()
# os.rename()
# os.path.exists()
# os.path.isfile()
# for root,dir,files in os.walk("."):
#     print(f"root -> {root}")
#     for file in files:
        # print(f"file names -> {file}")


#copy module
# 2 func are there on the copy module they are :(shalllowcopy, deepcopy)
# creates outer obj ,shares inner list(shallowcopy)
# occupies less memory space
# creates outer list obj,inner list also creates obj  |deep copy
import copy
# original=[[1,2,3],[4,5,6]]
# scopie_list=copy.copy(original)
# original[0][0]=17
# print(original)
# print(scopie_list)


# original=[[1,2,3],[4,5,6]]
# dcopy_list=copy.deepcopy(original)
# original[0][0]=17
# print(original)
# print(dcopy_list)

                                                                                                                                                                                                                                                                        