#isinstance
#The built in isinstance function lets you check if a variable matches a specific data type.
#It takes a value and the type you want to check it against, then returns a boolean.
#It also allows you to check for multiple types at once
account_balance = '12'
print(isinstance(account_balance, int))

account_balance_1 = 12
print(isinstance(account_balance_1,(int,float)))

#Report card
name = 'Bwalya'
print(name,type(name))
is_student = True
print(is_student,type(is_student))
age = 19
print(age,type(age))
score = 80.5
print(isinstance(score,float))
print(score,type(score))

#If you need a multiline string, a double or triple line string can be used
my_str_1 = """multiline String"""
print(my_str_1)

#String wrapping
print('He said, "won\'t l"')
print("becky said, \"hi\".")

#Escape sequences
print("Hello\nworld")
print('Name:\tAlice')
print('c:\\users\\Alice')

# 'in' operator to check if a string contains one or more characters
my_str_2 = 'hi world'

print('hello' in my_str_2)
print('hi' in my_str_2)
print('hey' in my_str_2)
print('o' in my_str_2)

# 'len' to check the length of a string

print(len(my_str_1))
print(len(my_str_2))

#checking the index(it is the position of character, it is also zero based) of a character using ( [] )

print(my_str_1[4])
print(my_str_2[7])

print(my_str_1[-2])
print(my_str_2[-4])

# Mutable & immutable values

name = 'john'
name = 'kyle'
print(name)

name = 'john'
name[0] = 'J'
# This will FAIL because strings are immutable
#name [0] = 'J' -> TypeError

#instead, you have to make a new string:

name='J' + name[1:]
print(name) #John
