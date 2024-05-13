print("hello world")
#creating variables uin python
# JS let or const, boolean or all other ones
name = "Kevin"
last_name = "Aguinaga"
age = 100
found = True
print ("My age is "+ str(age))

# if / else statements
# if(age < 100){cosnole.log("no woreries youre not that old")}
# javascript version 
if age < 99:
    print("Dont worry youre not that old") 
elif age > 101:
    print("Congrats youre a century old")
else: 
    print("I dont know how you get here!")
    
print("Im outside of the if statement")


#functions
# function name_of_function() --> this is the JS
def say_hello():
    print("Hello world")

def say_good_bye(name):
    print("Good bye " + name)

#try to print "hello my name is" age " "and im from" country
def test(name, age, country):
    print("hello my name is " + name + " I am " + str(age) + " years old and im from " + country)

#call the function
say_hello()
say_good_bye(name)
say_good_bye(name)
test(name, age, "Panama")
