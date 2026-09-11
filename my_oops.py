# OOPS CONCEPT

# class Students:
#     schoolname='chaitanya school' #class variable
#     def __init__(self,sid,sname,sage):
#         self.sid=sid
#         self.sname=sname
#         self.sage=sage
#     def student_details(self):
#         print(f"--------student details------")
#         print(f"student id:{self.sid}")
#         print(f"student name:{self.sname}")
#         print(f"student age:{self.sage}")
#     def study(self):
#         print(f"{self.studentname} is studying 10th class...")
# s1=Students(6,'mahi',21)
# s1.student_details()


# class Students:
#     schoolname='chaitanya school' #class variable
#     def __init__(self,sid,sname,sage):
#         self.sid=sid
#         self.sname=sname
#         self.sage=sage
#     def student_details(self):
#         print(f"--------student details------")
#         print(f"student id:{self.sid}")
#         print(f"student name:{self.sname}")
#         print(f"student age:{self.sage}")
#         print(f"school name:{Students.schoolname}")
#     def study(self):
#         print(f"{self.sname} is studying 10th class...")
# s1=Students(6,'mahi',21)
# s2=Students(2,'manu',31)
# s2.study()
# s1.study()
# s1.student_details()

# # EMPLOYEE DATA

# class Employee:
#     def __init__(self,eid,ename,ejob,eloc):
#         self.eid=eid
#         self.ename=ename
#         self.ejob=ejob
#         self.eloc=eloc
#     def employee_details(self):
#         print("-----emp details-------")
#         print(f" employee id:{self.eid}")
#         print(f" employee name:{self.ename}")
#         print(f" employee job:{self.ejob}")
#         print(f" employee location:{self.eloc}")
# e1=Employee(101,'chaitu','developer','bangolore')
# e1.employee_details()
        
# # CLASS METHOD

# class Students:
#     schoolname='chaitanya school' #class variable
#     def __init__(self,sid,sname,sage):
#         self.sid=sid
#         self.sname=sname
#         self.sage=sage
#     @classmethod
#     def changeschool(cls,name):
#       cls.name=name
#       print(f"school name: {cls.name}")
      
#     def student_details(self):
#         print(f"--------student details------")
#         print(f"student id:{self.sid}")
#         print(f"student name:{self.sname}")
#         print(f"student age:{self.sage}")
#         print(f"school name:{Students.schoolname}")
#     def study(self):
#         print(f"{self.sname} is studying 10th class...")
# s1=Students(6,'mahi',21)
# s1.student_details()
# s1.study()
# Students.changeschool("hii school")

# # STATIC METHOD

# class Students:
#     schoolname='chaitanya school' #class variable
#     def __init__(self,sid,sname,sage):
#         self.sid=sid
#         self.sname=sname
#         self.sage=sage
#     @classmethod
#     def changeschool(cls,name):
#       cls.name=name
#       print(f"school name: {cls.name}")
    
#     @staticmethod
#     def marks(*mark):
#       print(f"total marks:{sum(mark)}")  
#     def student_details(self):
#         print(f"--------student details------")
#         print(f"student id:{self.sid}")
#         print(f"student name:{self.sname}")
#         print(f"student age:{self.sage}")
#         print(f"school name:{Students.schoolname}")
#     def study(self):
#         print(f"{self.sname} is studying 10th class...")
# s1=Students(6,'mahi',21)
# s1.student_details()
# s1.study()
# s1.marks(21,39)
# Students.changeschool("hii school")


# # NESTED CLASS

# class Car:
#   class Engine:
#     def start(self):
#       print("car engine is started...")
#   def __init__(self):
#     self.engine=Car.Engine()
#   def drive(self):
#     self.engine.start()
#     print("car is moving...")
# # c=Car.Engine()
# # c.start()
# c=Car()
# c.drive()

# class Computer:
#   class Processor:
#     def start(self):
#       print("computer processor is working...")
#     def __init__(self):
#       self.processor=Computer.Processor()
#     def proc(self):
#       self.processor.start()
#       print("computer is running...")
# c=Computer.Processor()
# c.start()
# c=Computer()
# c.proc()

# class Father:
#   def house(self):
#     print("my father has own house")

# class Child(Father):
#   def bike(self):
#     print("i have my own bike")
# c=Child()
# c.house()
# c.bike()

# class Father:
#   def __init__(self,fname,fcontactno):
#     self.fname=fname
#     self.fcontactno=fcontactno
#   def house(self):
#     print("my father has own house")
#   def parentdetails(self):
#     print(f"fther name:{self.fname}")
#     print(f"father contact number:{self.fcontactno}")

# class Child(Father):
#   def __init__(self,fname,fcontactno, cname, cage):
#     super().__init__(fname,fcontactno)
#     self.cname=cname
#     self.cage=cage
#   def bike(self):
#     print("i have my own bike")
#   def childdetails(self):
#     print(f"child name:{self.cname}")
#     print(f"child age:{self.cage}")
# c=Child("chaitu",5937246203,"mahi",22)
# c.house()
# c.bike()
# c.parentdetails()
# c.childdetails()


# class Employee:
#   def __init__(self,eid,ename,esalary):
#     self.eid=eid
#     self.ename=ename
#     self.esalary=esalary
    
#   def emp_details(self):
#     print(f"employee id:{self.eid}")
#     print(f"employee name:{self.ename}")
#     print(f"employee salary:{self.esalary}")
#   def work(self):
#     print(f"{self.ename} is working")
#   def meeting(self):
#     print(f"{self.ename} is attending meeting...")

# ob1=Employee(101,"mahi",82000)
# ob2=Employee(210,"chaitu",90000)
# ob1.emp_details()
# ob1.work()
# ob1.meeting()
# # ob2.work()
# # ob2.meeting()



# class Employee:
#   def __init__(self,eid,ename,esalary):
#     self.eid=eid
#     self.ename=ename
#     self.esalary=esalary
    
#   def emp_details(self):
#     print(f"employee id:{self.eid}")
#     print(f"employee name:{self.ename}")
#     print(f"employee salary:{self.esalary}")
#   def work(self):
#     print(f"{self.ename} is working")
#   def meeting(self):
#     print(f"{self.ename} is attending meeting...")
  
#   class Department:
#     def __init__(self,deptid,dname,loc,employee):
#       self.deptid=deptid
#       self.dname=dname
#       self.loc=loc
#       self.employee=employee
#     def dept_info(self):
#       print(f"department id:{self.deptid}")
#       print(f"department name:{self.dname}")
#       print(f"department location:{self.loc}")
#       self.employee.emp_details()      
# ob1=Employee(101,"mahi",82000)    
# d=Employee.Department(10,'sales','chennai',ob1)
# d.dept_info()      

# ob1=Employee(101,"mahi",82000)
# ob2=Employee(210,"chaitu",90000)
# ob1.emp_details()
# ob1.work()
# ob1.meeting()
# ob2.work()
# ob2.meeting()

# # single inhertence
# class Father:      
#     def house(self):
#         print("my father is havving a house")
        
# class Child(Father):
#     def coding(self):
#         print("child is a software developer")
# c=Child()
# c.house()
# c.coding()
# print(Child.__mro__)        
        
# # multiple inheritence:
# class Father:      
#     def house(self):
#         print("my father is havving a house")

# class Mother:
#     def gold(self):
#         print("my mother is having 1000kg gold")
        
# class Child(Father,Mother):
#     def coding(self):
#         print("child is a software developer")
        
# c=Child()
# c.house()
# c.gold()
# c.coding()
# print(Child.__mro__)

# # multilevel:

# class Grandfather:
#     def __init__(self,gname,gage):
#         self.gname=gname
#         self.gage=gage
#     def land(self):
#         print("my grandfather is having 100 acrs of land")
# class Mother(Grandfather):
#     def __init__(self,gname,gage,mname,mage):
#         super().__init__(gname,gage)
#         self.mname=mname
#         self.mage=mage
#     def house(self):
#         print("my mother is having a villa")   
#     def family_tree(self):
#         print(f"grand father name: {self.gname}")
#         print(f"grand father age: {self.gage}")   
#         print(f"mother name: {self.gname}")
#         print(f"mother age: {self.gage}")  
# class Child(Mother):         
#     def car(self):
#         print("child is having a defender")
# c=Child('simha','80','laxmi','40')  
# c.land()
# c.house()
# c.car()  
# c.family_tree()               

# # hierarchiel inheritence:
# class Father:
#     def house(self):
#         print("my father is having a house")
# class Child1(Father):
#     def gold(self):
#         print("my mother is having 10 kg gold")
# class Child2(Father):
#     def coding(self):
#         print("child is a software engineer")
# c1=Child1()
# c2=Child2()
# c1.gold()
# c1.house()
# c2.house()
# c2.coding()      


# # hybrid inheritence:
  
# class Grandfather:
#     def land(self):
#         print("my grandfather is having 100 acrs of land")                        
# class Father(Grandfather):
#     def house(self):
#         print("my father is having a house")
# class Mother(Grandfather):
#     def gold(self):
#         print("my mother is having 10 kg gold")
# class Child(Father,Mother):
#     def coding(self):
#         print("child is a software engineer")     
# c=Child()      
# c.land()
# c.house()
# c.gold()
# c.coding()                      


# class Employee:
#     companyname='google'
#     def __init__(self,empid,ename,esalary,loc):
#         self.ename=ename
#         self.empid=empid
#         self.esalary=esalary
#         self.loc=loc



# class Developer(Employee):
#     def __init__(self,empid,ename,esalary,role,lang,loc):
#         super().__init__(self,empid,ename,esalary,loc)
#         self.role=role
#         self.lang=lang
#     def devloper_info(self):
#         print(f"employee id:{self.empid}")
#         print(f"employee name:{self.ename}")
#         print(f"employee salary:{self.esalary}")
#         print(f"employee designation:{self.role}")
#         print(f"employee skills:{self.lang}")
#         print(f"employee loc:{self.loc}")
        
# class Manager        
      

# polymorphism--meaning(manyfroms)it allows the method name or operater name to behave differently based on the obj or datatype with.
# class Animal: 
#   def speak(self):
#       pass
# class Dog(Animal):
#   def speak(self):
#       print('bow bow')
# class Cat(Animal):
#   def speak(self):
#       print('meow meow')

# d=Dog()          
# c=Cat()  

# d.speak()
# c.speak()


# class Calculator:
#   def add(self,a=None,b=None,c=None):
#       if a is not None and b is not None and c is not None:
#         print(f"three parameters adding : {a+b+c}")
#       elif a is not None and b is not None:
#         print(f"two parameters adding : {a+b}")
#       else:
#         print("pass atleast 2 parameters")
# c=Calculator()
# c.add(20,30)
# c.add(10,20,30)        

# class Calculator:  "kargs method"
#   def add(self,*args):
#       total=0
#       for value in args:
#           total+=value
#       print(f"sum: {total}")
                           
# c=Calculator()
# c.add(20,30)
# c.add(10,20,30)                 
# c.add(10,20,30,40)
# c.add(10,20,30),40,50                


# class Students:
#   def __init__(self,sub1,sub2):
#       self.sub1=sub1
#       self.sub2=sub2
      
#   def __str__(self):
#       print(f"sub1 value is {self.sub1}")
#       print(f"sub2 value is {self.sub2}")
#   def __add__(self,other):
#       print(f"adding two objects datas :({self.sub1+other.sub1},{self.sub2+other.sub2})")
      
# s1=Students("rana",80)
# s2=Students("reddy",90) 
# result=s1+s2
# print(result)             


# class Bank:
#     def __init__(self, name, rate_of_interest, amount, years):
#         # Private attributes (encapsulation)
#         self.__name = name
#         self.__rate_of_interest = rate_of_interest
#         self.__amount = amount
#         self.__years = years

#     # Getter methods
#     def get_name(self):
#         return self.__name

#     def get_rate_of_interest(self):
#         return self.__rate_of_interest

#     def get_amount(self):
#         return self.__amount

#     def get_years(self):
#         return self.__years

#     # Setter methods
#     def set_rate_of_interest(self, rate):
#         self.__rate_of_interest = rate

#     def set_amount(self, amount):
#         self.__amount = amount

#     def set_years(self, years):
#         self.__years = years

  
#     def calculate_interest(self):
#         interest = (self.__amount * self.__rate_of_interest * self.__years) / 100
#         return interest


# sbi = Bank("SBI", 6.5, 100000, 5)
# icici = Bank("ICICI", 7.0, 150000, 3)
# hdfc = Bank("HDFC", 6.8, 200000, 4)

# banks = [sbi, icici, hdfc]

# for bank in banks:
#     print(f"Bank: {bank.get_name()}")
#     print(f"Rate of Interest: {bank.get_rate_of_interest()}%")
#     print(f"Amount: {bank.get_amount()}")
#     print(f"Years: {bank.get_years()}")
#     print(f"Calculated Interest: {bank.calculate_interest()}")
#     print("-" * 40)


# duck typing: interpreter or compiler doesent care about your class or obj if any method it quack like as a duck,walk like as a duck its a duck typing.

# class Duck:
#   def fly(self):
#       print("Duck is flying")
# class Aeroplane:
#   def fly(self):
#       print("Aeroplane is flying")
# class Bird:
#   def fly(self):
#       print("bird is flying")
# def flying_obj(object):
#     object.fly()
# D=Duck()
# B=Bird()
# A=Aeroplane()
# flying_obj(D)  
# flying_obj(B)
# flying_obj(A) 
                                    

# Absttraction:hide complex implementation and shows only neccesary features or options of an object to the users.
# from abc import ABC,abstractmethod

# class paymentprocess(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
# # implementation hiding
# class CreditCardPayment(paymentprocess):
#     def pay(self,amount):
#         print(f"processing credit card payment of {amount:,}...") 
#         print("payment is successful via credit card 🌟")
# class PayPalPayment(paymentprocess):
#     def pay(self,amount):
#         print(f"processing PayPal payment of {amount:,}...")
#         print("payment is successful via PayPal🌟")  
# class cryptocurrencyPayment(paymentprocess):
#     def pay(self,amount):
#         print(f"processing cryptocurrency payment of {amount:,}...")
#         print("payment is successful via cryptocurrency🌟")
# # client side app        
# class shoppingcart:
#     def __init__(self,paymentmethod:paymentprocess):
#         self.paymentmethod = paymentmethod
#     def checkout(self,amount):
#         print(f"final amount payed by user through : {amount:,}")
#         self.paymentmethod.pay(amount)
# my_creditcard=CreditCardPayment()
# my_paypal=PayPalPayment()
# my_cryptocurrency=cryptocurrencyPayment()

# cart=shoppingcart(my_creditcard)
# cart.checkout(10000)

# class Notification(ABC):
#     @abstractmethod
#     def send_notification(self,message):
#         pass
      
# class EmailNotification(Notification):
#     def send_notification(self,message):
#         print(f"Sending email notification: {message} 📧")
# class SMSNotification(Notification):
#     def send_notification(self,message):
#         print(f"Sending SMS notification: {message} 📱")
# class InstagramNotification(Notification):
#     def send_notification(self,message):
#         print(f"Sending Instagram notification: {message} 📷")
# class WhatsAppNotification(Notification):
#      def send_notification(self,message):
#         print(f"Sending WhatsApp notification: {message} 💬") 
# def send_notification_to_user(notification:Notification,message):
#     notification.send_notification(message)
#     print("notification sent successfully ✅")
# email_notification=EmailNotification()
# sms_notification=SMSNotification()
# instagram_notification=InstagramNotification()
# whatsapp_notification=WhatsAppNotification()
# send_notification_to_user(email_notification,"your order has been shipped")
# send_notification_to_user(sms_notification,"your order has been shipped")
# send_notification_to_user(instagram_notification,"your order has been shipped")
# send_notification_to_user(whatsapp_notification,"your order has been shipped")
# my_notification=EmailNotification()
# my_notification.send_notification("your order has been shipped")
# my_emailnotification=EmailNotification()
# my_whatsappnotification=WhatsAppNotification()
# send_notification_to_user(my_emailnotification,"your order has been shipped")
# send_notification_to_user(my_whatsappnotification,"your order has been shipped")
# my_instagramnotification=InstagramNotification()
# send_notification_to_user(my_instagramnotification,"your order has been shipped")
# my_smsnotification=SMSNotification()
# send_notification_to_user(my_smsnotification,"your order has been shipped")
