# def counter(n):
#     if n==0:
#         return 1
#     print(n)
#     counter(n-1)
# counter(5)  


def fact(i):
    if i==0 or i==1:
        return 1
    return i*fact(i-1)
# print(fact(10))    

# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1)+fib(n-2)
# for i in range(5):
#     print(fib(i),end="")

