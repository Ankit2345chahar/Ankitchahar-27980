#num1 = int(input("enter the first number"))
#num2 = int(input("enter the second number"))
#if num1>num2 :
 #    print(num1,"is greater")
##elif num2>num1 :
  #   print(num2,"is greater")
#else :
 #    print("both are equal")



# gender = input("which type of gender: ")
# if gender == "male":
#      print("good morning sir")
# else:
#      print("good morning maam")


# num = int(input("enter the number to check even or odd:-"))
# if num%2 ==0:
#     print(num,"is even")
# else:
#     print(num,"is odd")


# name = input("enter your name:-")
# voter_age = input("enter your age:-") 
# if int(voter_age) >= 18:
#     print("you are eligible for voting",name)
# else:
#     print("you are not eligible for voting",name)



# year = int(input("enter the year"))
# if year%100 == 0 and  year%400 ==0:
#     print(year,"is a leap year")
# elif year%4  ==0:
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")



# temperature = int(input("enter the temperature"))
# if temperature<=00:
#     print("freezing weather")
# elif temperature>0 and temperature<=10:
#     print("very cold weather")
# elif temperature>10 and temperature<=20:
#     print("cold weather")
# elif temperature>20 and temperature<=30:
#     print("normal in temperature")
# else:
#     print("hot")


# a = range(1,21,1)
# for i in a:
#     print(i)
  
# if i%2==0:
#     print(a,"is even")
# else:
#     print(a,"is odd")
# for i in range(1,101,5):
#     print(i)
# for i in range(16,0,-1):
#     print(i)
       

# for i in range(-3,-15,-1):
#     print(i)


#p lets a print n users through tables
# n = int(input("which table you want to print:-"))
# for i in range(n, (n*10)+1, n):
#   print(i)

# a = "i am army officer, its my duty to serve my country"
# print(len(a))
# for i in range (len(a)):
#  print(a[i])

# a = "i am army officer, its my duty to serve my country"
# for i in a:
#     print(i)

# for i in range(1,21):
#     if i == 25:
#         print("break statement excuted")
#         break
#     print(i)
# else:
#     print("break statement not executed")



# loop question 
# n = int(input("please enter the number:-"))
# for i in range(n):
#     print("hello world")

# n = int(input("please enter the natural number:-"))
# for i in range(1,n+1):
#     print(i)

# n = int(input("please tell your number:-"))
# for i in range (n,0,-1):
#     print(i)

# n = int(input("please enter the table you want to print:-"))
# for i in range(n,(n*10)+1):
#  print(i)
# else:
#  print("table printed successfully")

# n = int(input("please enter the table you want to print:-"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")
# else:
#     print("table printed successfully")

# n = int(input("please enter the number:-"))

# sum = 0

# for i in range(1,n+1):
#  sum = sum + i

#  print(f"your sum is {sum}")




# n = int(input("please enter the number:-"))

# fact = 1

# for i in range(1,n*1):
   
#    fact = fact * i

# print(f"your fact is {fact}")


# n = int(input("please enter the number:-"))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2==0:
#         even = even + i
#     else:
#         odd= odd + i
#         print(f"your number is even {even}")
#         print(f"your number is 0dd {odd}")

# n = int(input("which number factors you want:-"))
# for i in range (1,n+1):
#     if n%i==0:
#         print(i)


# n = int(input("check your number is perfect or not:-"))
# sum = 0
# for i in range(1,n):
#     if n%i==0:
#         sum = sum + i

#         if  sum ==n:
#             print(f"your number is pefect")
#         else:
#             print(f"your number is not perfect")


# n = int(input("check your number is prime or not:-"))

# count = 0

# for i in range (1,n+1):
#     if n%i==0:
       
#         count = count + 1

# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")



# a = "i am army officer, its my duty to serve my country" 
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
    
#     if b==a:
#         print("yourstring is palindrome")
#     else:
#         print("your string is not palindrome")


# a = "sffllk@^&89376667jkkolkjjbklkjlsl1234@@@&&&******8834s"
# char = 0
# dig = 0
# spchr = 0
# for i in a:
#     if i.isalpha():
#         char +=  1
#     elif i.isdigit():
#         dig += 1
#     else:
#         spchr += 1
#         print(f"your digits are {dig}\n your alphabets are {char}\n your special characters are {spchr}")


# a = int(input("enter the number:-"))
# while a>0:
#   print(a%10)
#   a= a//10
    


# a = int(input("enter the number:-"))
# rev = 0
# while a>0:
#     rev= rev * 10 + a % 10
#     a = a // 10
#     print(rev)







# a = int(input("enter the number:-"))
# copy = a
# rev = 0
# while a>0:
#     rev= rev * 10 + a % 10
#     a = a // 10

#     if copy == rev:
#         print("your number is palindrome")
#     else:
#         print("your number is not palindrome")
    
      


# import random
# num = random.randint(1,10)
# print(num)
# guess = int(input("enter your guess number between 1 to 10:-"))

# if num ==guess:
#     print("your guess is correct")
# else:
#     print ("your guess is incorrect") 



# print("hello bro how are you")


# def hello():
#     print("i am army officer and its my duty to serve my counrty")

# hello()


# def sum(a,b):
#     print(f"the sum of your numbers is {a+b}")

# sum(12,12)
# sum(45,45)
  
# def hello(name,age):
#     print(f"hello {name} your age is {age}")

# hello(age = 21, name = "Ankit")




# def pallindrome(st):
#     rev = ""  # Initialize rev
#     for i in range(len(st)-1, -1, -1):
#         rev = rev + st[i]
#     if rev == st:
#         print("your string is pallindrome")
#     else:
#         print("your string is not pallindrome")

# pallindrome("madam")
# pallindrome("ankit")



# def hello():
#     return"hello bro how are you"

# print(hello())



# DATA STRUCTURE IN PYTHON  
# LIST IN PYTHON
a = [12, 23, 24, 22, "true", "ankit"]
print(a[2])
print(a[3])
print(a[::])

