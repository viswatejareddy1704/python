# n=8
# for row in range(n):
#     for column in range(n):
#         print("*",end=" ")
#     print()    


# n=5
# for rows in range(1,n+1):
#     for spaces in range(n-rows):
#         print(" ",end=" ")
#     for stars in range(rows):
#         print("*",end=" ") 
#     print()    

# n=5
# for rows in range(1,n+1):
#     for stars in  range(rows):
#         print("*",end=" ")
#     print()    
        
# n=5
# for rows in range(1,n+1):
#     for stars in range(rows):
#         print(chr(96+rows),end=" ")
#     print()    

# n=5
# for row in range(n):
#     for space in range(n-row):
#         print(" ",end=" ")
#     for star in range(2*row+1):
#         print("*",end=" ")
#     print()        

# n=5
# for row in range(n):
#     for spaces in range(row):
#         print(" ",end=" ")
#     for stars in range(2*(n - row) -1):
#         print("*",end=" ")
#     print()        

# n=5
# for row in range(1,n+1):
#     for spaces in range(n-row):
#         print(" ",end=" ")
#     for stars in range(2*row-1):
#         print("*",end=" ")
#     print()
# for row in range(n-1,0,-1):
#     for space in range(n-row):
#         print(" ",end=" ")
#     for stars in range(2*row-1):
#         print("*",end=" ")
#     print()        

# n=5
# for row in range(n,0,-1):
#     for spaces in range(n-row):
#         print(" ",end=" ")
#     for stars in range(2*row-1):
#         print("*",end=" ")
#     print()
# for row in range(1,n+1):
#     for space in range(n-row):
#         print(" ",end=" ")
#     for stars in range(2*row-1):
#         print("*",end=" ")
#     print()        



# rows = 5
# cols = 5
# for row in range(rows):
#     for col in range(cols):
#     if row==0 or row==rows-1 or col==0 or col==cols-1:
#         print("*",end=" ")
#     else:
#         print(" ",end=" ")
#     print()        
        
# n=int(input("enter the number"))
# if n%2==0:
#     print(f"{n} even number")
# else:
#     print(f"{n} odd number")    
 
# n=-7
# if n>0:
#     print(f"{n} is positive number")
# elif n<0:
#     print(f"{n} is negative number")
# else:
#     print(f"{n} is zero number")    
            
# v1=15
# v2=13
# v3=22

# if v1>v2 and v1>v3:
#     print(f"{v1} is greater than {v2} & {v3}")
# elif v1>v2>v3:
#     print(f"{v2} is greater than {v1} & {v3}")
# else:
#     print(f"{v3} is greater than {v1} & {v2}")                    

# v1=20
# v2=30
# print(f"before swap v1:{v1} & v2{v2}")
# v1,v2=v2,v1
# print(f"after swap v1:{v1} & v2:{v2}"

# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print(f"iteration:{i} & fact result:{fact}")
# print(f"5! factorial: {fact}")    


# n=int(input("enter the number:"))
# original_value=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# if original_value==rev:
#     print("palindrome")
# else:
#     print("not palindrome")   

# n=int(input("enter the number:"))
# a=0
# b=1

# for i in range(1,n+1):
#     print(a,end=" ")
#     a,b=b,a+b

# n=int(input("enter the number:"))
# if n<1:
#     print("not prime number")
# else:
#     has_prime=True 
#     for i in range(2,n):
#         if n%i==0:
#             has_prime=False
#             break
#     if has_prime:
#         print("prime number")
#     else:
#         print("not prime number")    

# n=int(input("enter the number:"))

# original_value=n
# sum=0
# length=len(str(n))
# while n>0:
#     digit=n%10
#     sum+=digit**length
#     n//=10
# if original_value==sum:
#     print(f"{original_value} is a armstrong number")
# else:
#     print(f"{original_value} is not a armstrong number")    
    
# n=int(input("enter the number:"))
# sum_digits=0
# while n>0:
#     digit=n%10
#     sum_digits+=digit
#     n//=10
# print(sum_digits)    
    
# n=int(input("enter the nunmber:"))    
# sum=0

# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("perfect number")
# else:
#     print("not a perfect number")               
       
# n=int(input("enter the nunmber:"))   
# temp=n
# sum=0

# while n>0:
#     digit=n%10
#     fact=1
#     for i in range(1,digit+1):
#         fact*=i
#     sum+=fact
#     n//=10
# if temp==sum:
#     print("strong number")
# else:
#     print("not strong number")            
 


     