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
# a = [12, 23, 24, 22, "true", "ankit"]
# print(a[2])
# print(a[3])
# print(a[::])

#  1st way method indexing 
# a = [12, 23, 24, 22, "true", "ankit"]
# for i in range(len(a)):
#     print(i)

# for i in range(len(a)):
#     print(a[i])



# #2nd way method
# for i in a:
#     print(i)


# a = [8,7,9,0,0,True,"@"]
# print(a[0:4])

# print(dir(list))


# append
# l = [2,4,66,99,8]
# l.append(6)
# print(l)

# insert 
# l = [1,3,4,5,6]
# l.insert(1,2)
# print(l)

# help(list)

# remove
# l =[1,2,3,4,5,6]
# l.remove(1)
# print(l)

# change a value 
# l = [2,2,3,4,5,6,7,8,9]
# l[0]=1
# print(l)

# Print positive and negative elements of an List

# l = [1,2,3,4,5,-6,-8,-9,-33,55,22,8,-8]
# print("postive element")
# for i in l:
#    if i>0:
#       print(i)
#       print("negative element")
#       for i in l:
#          if i<0:
#             print(i)
 

# Mean of List elements

# l = [22,44,66,888,33,999,22,66,333,444,8865,44,2,44,33]
# sum = 0
# for i in l:
#     sum = sum + i
#     print(sum/len(l))
  

# Taking input from user

# numbers = list(map(float, input("Enter the number find a list  mean:-").split()))
# mean = sum(numbers) / len(numbers)
# print("Mean of the list elements is:", mean)



# Find the greatest element and its index

# l = [22, 444, 22, 6, 88, 77, 234, 887, 888, 987, 1000, 33, 66, 99, 33, 55, 888]
# largest = 0
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"Your largest number is {largest} at index {index}")


# Find the second greatest element.

# l = [12,14,16,12,44,66,55,44,33,22,89,67]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest and i != largest:
#         sec_largest = i

# print(f"Largest number: {largest}")
# print(f"Second largest number: {sec_largest}")
   


 #Check if List is sorted or not.

# a = [12,13,14,15,16]
# for i in range(len(a)-1):
#     if a [i] < a [i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your listed is sorted")

# tuple data structure

# a =(1,2,3,4)
# print(type(a))

        
# a = (1,2,3,4,5,6,True, "hello")
# for i in a: # for i in range(len(a))
#     print(i)


# a =(1,2,3,4,5,6,7,8,3,4,5,65,5,5,5)
# # index = a.index(65)
# # print(index)

# count =a.count(5)
# print(count)

#set 
# s = {1,2,3,4,5,6,6,5,4,3,2,1}
# print(type(s))
# print(s)

# a = {1,8,9,"helllo",3,5,6,7,8}
# for i in a:       #  for i in range(len(a)):
#     print(i)

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# s = a.symmetric_difference(b) #a.union(b) , a.intersection(b) , a.difference(b)
# print(s)


# dictiionary 

# d = {1:4,2:"hello"}
# print(type(d))
# print(d[2])

# d = {1:100,2:200,3:300,4:"hello"}
# for i in d:
#     print(d[i]) # print(i)
     
# a = {1,2,3,4}
# b = a
# b.remove(1)
# b.add(20)
# print(a)


# question in dictionary

#  Write a Python script to merge two Python dictionaries.

# d1 = {10:100, 20:200, 30:300}
#  d2 = {40:400, 50:500, 60:600}

#  d1.update(d2)
#  print(d1)

# Write a Python program to sum all the values in a dictionary
# d1 = {10:100, 20:200, 30:300}
# sum = 0
# for i in d1:
#  sum = sum + d1[i]
# print(sum)


# Count the frequency of each elements

# a = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,9,9,9]
# d = {}
# for i in a:
#   if i in d.keys():
#     d[i] += 1
#   else:
#     d[i] = 1
# print(d)



# Write a Python program to combine two dictionary by adding values for common keys.

# d1 = {10:100, 20:200, 40:300}
# d2 = {40:400, 50:500, 60:600}
# for i in d2:
#     if i in d1:
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)






