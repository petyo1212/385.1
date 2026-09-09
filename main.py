#Python redux. We get to know the scripting, comments and running files
# My first comment
'''
Multiline comments
Python is read top to bottom and left to right. Complex logic being on sequence.
Concurency is not allowed in Python, acts like single treaded. 
Losly typed language
'''
print ("Hello, World!")
'''
PRimitive data types
string - text surronded by quotes '' or '
Number:
    integer int whole numbers discrete
    float 
boolean bool
variable is like a container and use name to grab the info inside
naming convection: no start with numbers, only _ , no reserve words, no spaces, case sensitive, should be clear what is variable with.
MUst start with letter or _ 
USe snake case or camel case
'''
fav_number = 13
says= "Jony said \"HEllo!\"" #Use opposite qutes or escape
# To inject variable in print use f'{variable}'
print(says , f'three times {says}', fav_number)
print(fav_number)

#Input function - gets input from user in terminal. Use paretneses 
name=input("What is your name?")
age=input("What is your age?")
print(f'Are you saying your name is {name} and you are {age} old?')

#End of file

