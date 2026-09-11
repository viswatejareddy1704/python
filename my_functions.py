# def greet():
#     print("hello")
#     print("world")
#     print("welcome")
# greet()
# greet()
# greet()
# greet()    

# def addition():
#     return 30+50
      
# print(addition())
# res=addition()
# print(res)

# def add(a,b):
#     return a+b
# print(add(10,2))

# def sub(a,b,c):
#     return a-b-c
# print(sub(c=30,a=10,b=20))

# def add(a,b,c=5):
#     return a+b+c
# print(add(10,b=20))

# def add(*a):
#     return sum(a)
# print(add(10,20,30,40,50,60,50))

# def emp(*names):
#     print(names)
# emp("mahesh","vinay","arjun","deva","rudra")    

# def emp(**details):
#     print(details)
# emp(empid=1020,salary=55000,job="devops engineer",loc="banglore") 

# def employee_details(empid,ename,sal=53000,*contactnos,**additioninfo):
#     print(f"=============employee details========")
#     print(f"employee id: {empid}")
#     print(f"employee name: {ename}")
#     print(f"employee salary: {sal}")
#     print(f"employee contactnumbers: {contactnos}")
#     print(f"employee addition info: {additioninfo}")
# employee_details(111,"ugradevranareddy",65000,985762304327,476420345670,loc="banglore",pincode=518273)       

# def addition(a,b):
#     return a+b
# def subtraction(a,b):
#     return a-b
# def multiplication(a,b):
#     return a*b 
# def division(a,b):
#     return a/b 
# def power(a,b):
#     return a**b
# def modulus(a,b):
#     return a%b
# def flrdiv(a,b):
#     return a//b

# def calculator():
#     while True:
#         choice=int(int(input("entr the user choice(1-7):")))
#         a=int(input("enter a value:"))
#         b=int(input("enter a value:"))
#         if choice==7:
#             print("user chooses a choice exit... thank you user")
#         elif choice==1:
#             result=addition(a,b)  
#             print(f"addtion: {result}")  
#         elif choice==2:
#             result=subtraction(a,b)
#             print(f"subtraction: {result}")  
#         elif choice==3:
#             result=multiplication(a,b)
#             print(f"multiplication: {result}")
#         elif choice==4:
#             result=division(a,b)
#             print(f"division: {result}")
#         elif choice==5:
#             result=power(a,b)
#             print(f"power: {result}")
#         elif choice==6:
#             result=modulus(a,b)
#             print(f"modulus: {result}")
#         elif choice==7:
#             result=flrdiv(a,b)
#             print(f"flrdiv: {result}")
# calculator()            
                        
                 
# name="ugradevranareddy"
# def add_info(contactno):
#     global name
#     name="rudra"
#     emailid="ugradevranareddy1704@gmail.com"
#     print(name)
#     print(contactno)
#     print(emailid)
# add_info(8975462435)    
# print(name)                       


# nested frunctions
# def outer():
#     print("mother of deva ")
#     def inner():
#         print("son of reddy")
#     inner()     
# outer()    

# def outer():
#     x=17
#     def inner():
#         nonlocal x
#         y=21
#         x=4
#         print(x)
#         print(y)
#     inner()
#     print(x)
# outer()    

# def counter():
#     c=0
#     def increment():
#         nonlocal c 
#         c+=1
#         print(f"local variable accessing with in inner func: {c}")
#     increment()
#     #print(f"local variable: {c}")
# counter() 
# counter()
# counter() 
# counter()      

# x=100           #global variable
# def outer():    
#     y=200        #non local for inner function 
#     global x
#     x+=1000     
#     def inner():
#         z=300      #local variable
#         nonlocal y
#         y+=300
#         print(x)
#         print(y)
#         print(z)
#     inner()
# outer()      

# bankname="sbi"
# def account():
#     balance=1500
#     def deposit(amount):
#         nonlocal balance
#         balance+=amount
#         print(f"bank name: {bankname}")
#         print(f"current account balance: {balance}")
#     deposit(10000)      
# account()    

#lamba function
# v=lambda x:x*x
# print(v(4))

# marks=[90,86,68.70,62,86]

# extramarks=list(map(lambda x:x+5,marks))
# print(extramarks)

# names=["ugra","dev","rana","rudra","arjun"]

# uppercase=list(map(lambda name:name.upper(),names))
# print(uppercase)

# nums=[2,5,4,3,1]

# square=list(map(lambda x:x**2,nums))
# print(square)

# salaries=[35000,85000,9000,60000,70000]

# deduction=list(map(lambda x:x-(x*0.18),salaries))
# print(deduction)

# the filter items which is satisfied based on the condition


# salaries=[35000,85000,9000,60000,70000]

# f_salary=list(filter(lambda x:x>60000,salaries))
# print(f_salary)

# nums=[1,2,3,4,5,6,7,8,9,10]

# f_nums=list(filter(lambda x:x%2==0,nums))
# print(f_nums)

# reduce reduces sequence of a value into a single value

# from functools import reduce
# n=[1,2,3,4,5]
# r=reduce(lambda x,y:x+y,n)
# print(r)

# salaries=[35000,85000,9000,60000,70000]
# s=sorted(salaries,key=lambda x:x)
# print(s)


# fruits=("guauva","apple","banana","grapes","pineapple","promagranete","strawberry","pears")

# fruits_sorted=sorted(fruits,key=lambda x:len(x))
# print(fruits_sorted)

