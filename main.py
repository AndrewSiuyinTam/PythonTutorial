# name = "bro"
# print("Hello" + name)

# age = 21
# age +=1
# print("Your age is" + str(age))
# # Types are string, ints, floats, and booleans. Variables are just container for values. Might need to do some casting

# # Multiple Assignment - allows us to assign multiple variables at the same time in one line of code
# name = 'bro'
# age = 21
# attractive = True
# name,age,attractive = 'bro',21,True

# # Dad = 30
# # Mom = 30
# # Me = 30
# Dad=Mom=Me = 30
# print(Mom)


# # String Methods

# name = "Bro"
# print(len(name))
# print(name.find("o"))
# print(name.capitalize())
# print(name.upper())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o,","a"))
# print(bro*3)

# # Type Casting
# x = 1
# y = 2.0
# z = "3"
# x = float(x)

# User input
# name = input("what is your name?: ")
# age = int(input("How old are you? "))
# height = float(input("How tall are you?"))
# print("Hello " + name)

# numbers
# import math
# x=1
# y=2
# z=3
# pi = 3.14
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(math.sqrt(pi))
# print(max(x,y,z))

# # String Slicing = create a substring by extracting elements from another string
# #[start:stop:step]

# name = "Andrew Tam"
# first_name = name[0:3:1]
# reversed_name = name[::-1] # Same as [0:end:-1]
# print(first_name)
# print(reversed_name)
# website = "http://google.com"
# slice = slice(7,-4)
# print(website[slice])

# if statement
# 5

## logical operators - used to check if two or more conditional statements are true
# temp = int(input("What is the temperature outside?: "))
# if temp >=0 and temp <=30:
#     print("the temperature is really cold outside")
# elif not( temp < 0 or temp > 30) :
#     print("THe temperature is bad today ")

# WHile Loops
# name = ""
# while len(name) == 0:
#     name = input("Enter Your name")

#     ## FOr loop is limited, while loop CAN be unlimited
#     for i in range(50,100):
#         print(i)

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)


# Nested Loops

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?"))
# symbol = input("Enter a symbol")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol,end="")
#     print()

#     # Loop Control Statements - changes a loop execution from its normal sequence

#     # break = terminate the loop entirely
#     # continue - skips to next iteration of the loop
#     # pass = does nothing, acts as a placeholder 

#     # list, array
#     food = ['pizza','hamburger','hotdog','spaghetti']
#     print(food[0])
#     food.append('ice cream')
#     food.remove("hotdog")
#     food.pop()


#     # 2D lists = a list of lists

#     drinks = ['coffee','soda','tea']
#     dinner = ['pizza','hamburger','hotdog']
#     dessert = ['cake','ice cream']
#     food = [drinks,dinner,dessert]
#     print(food[1][2 ])
#     # Can access just one of these lists if you want

#     # tuple = collection which is ordered and unchangeable, used to group together related data

#     student = ('Bro',21,False)
#     print(student.count("Bro"))
#     print(student.index("male"))

#     for x in student:
#         print(x)

# # sets - unoredred, unindexed, no duplicate values
# utensils = {'fork','spoon'}
# utensils.add()
# utensils.remove()
# # add one set to the other
# utensils.update(dishes)
# print(utensils.difference(utensils))

# dictionary = A changeable, unordered collection of unique key:value pairs. They are fast because they use hashing, allow us to access a value quickly 
# capitals  = {'USA':'Washington DC'}
# print(capitals['Russia'])
# print(capitals['germany']) # 
# # Much safer way to access a key is to use get in case the key is not there
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items()) # print out everything in dictionary

# for key, value in capitals.items():
#     print(key,value)

# capitals.update({'germany':'Berlin'})
# capitals.update({'Washington':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# Index Operator
# name = "Andrew Tam"
# if (name[0].islower()):
#     name = name.capitalize()
# first_name = name[0:3].upper()
# print(first_name)
# print(first_name[-1])

# # Function
# def hello():
#     print('hello')

# # Return

# def multiply(number1,number2):
#     result = number1 * nnumber2
#     return result



# Positional Arguments - order of arguemtns do matter
def hello(first,middle,last):
    print(first + middle + last)

# Keyword arguments - order of arguments doesnt matter
hello(last ='Code',middle='Dude',first = 'Bro')

# Nested function calls
print(round(abs(float(input("enter a positive number")))))

# scope
def display_name():
    name = "COde"
    print(name)


# *args - parameter that will pack all arguments into a tuple. useful so thata function can accept a varying amount of arguments