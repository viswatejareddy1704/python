# s="python"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)    

# s="python"
# count=0
# for ch in s:
#     count+=1
# print(f"characters count of {s} is : {count}")

# s=(input("enter a string:"))
# ch=""
# if ch==s:
#     print("empty str found")
# else:
#     print("not empty")         

# n=input("enter the string")
# v=0
# c=0
# for i in n:
#     if i in"aeiou":
#         v+=1
#     elif i.isalpha():
#         c+=1
# print(f"vowels count: {v}")
# print(f"consonants count: {c}")        
            
# n=input("enter the string")
# v=0
# c=0
# d=0
# s=0
# l=0
# u=0
# for i in n:
#     if i in "aeiou":
#         v+=1
#     elif i.isalpha():
#         c+=1
#     elif i.isdigit():
#         d+=1
#     elif i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1
#     else:
#         s+=1
# print(f"vowels count: {v}") 
# print(f"consonents count: {c}")                                        
# print(f"digits count: {d}")
# print(f"upper count: {u}")
# print(f"lowwer count: {l}")                                        
# print(f"special count: {s}")                                        
                                                                                     
# s=input("enter the strings:")
# rev=s[::-1]
# if s==rev:
#     print("palindrome")
# else:
#     print("not palindrome")   

# s=input("enter the string:")
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d) 

# s=input("enter the string:").split()
# largest=""
# for word in s:
#     if len(word)>len(largest):
#         largest=word
# print(f"largest word: {largest}")                       
             
# word1=input("enter the string:")
# word2=input("enter the string:")
# if sorted(word1)==sorted(word2):
#     print("anagram")
# else:
#     print("not anagram")                                                
     
# s=input("enter the string:")
# check=set()

# for ch in s:
#     if ch.isalpha():
#         check.add(ch)
# print("pangram" if len(check)==26 else "not pangram")        