# list ---> array
color = ["white","red","yellow"]

#add
color.append("pink")
print(color)

#for loop
for current in color:
    print(current)
    # for(i=0,i<color.length;i++)
    # current_p = color[i]

#Dictionaries
me ={
    "first_name": "Adrian",
    "last_name": "Aguinaga"
    # "age": 37
}


#get a value
print(me["first_name"])
print(type(me))
#add
me["color"] = "blue"
#modify
me["color"]="red"
me["age"]=50

print(me)
print(me["first_name"]+" "+me["last_name"]+" "+str(me["age"]))
print(color[1], color[3])

#EXAMPLE
ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]
# print all the numbers
#print all the numbers greater than 21
#print how many numbers are grater than 21
def printall():
    count = 0
    for age in ages:
        if age > 21:
            print(age)
            count += 1
    print("There was "+ str(count) + " greater than 21")

#Call the function
printall()

users = [
   {
       'id': 1,
       'name': 'Alice',
       'gender': 'female',
       'age': 25,
       'preferred_color': 'blue'
   },
   {
       'id': 2,
       'name': 'Bob',
       'gender': 'male',
       'age': 35,
       'preferred_color': 'GREEN'
   },
   {
       'id': 3,
       'name': 'Charlie',
       'gender': 'male',
       'age': 45,
       'preferred_color': 'Red'
   },
   {
       'id': 4,
       'name': 'Danielle',
       'gender': 'female',
       'age': 30,
       'preferred_color': 'YelloW'
   },
   {
       'id': 5,
       'name': 'Evelyn',
       'gender': 'female',
       'age': 20,
       'preferred_color': 'PuRplE'
   },
   {
       'id': 6,
       'name': 'Frank',
       'gender': 'male',
       'age': 28,
       'preferred_color': 'purple'
   },
{
       'id': 7,
       'name': 'Grace',
       'gender': 'female',
       'age': 31,
       'preferred_color': 'GREEN'
   },
   {
       'id': 8,
       'name': 'Henry',
       'gender': 'male',
       'age': 40,
       'preferred_color': 'BLUE'
   },
   {
       'id': 9,
       'name': 'Isabelle',
       'gender': 'female',
       'age': 27,
       'preferred_color': 'red'
   },
   {
       'id': 10,
       'name': 'Jack',
       'gender': 'male',
       'age': 24,
       'preferred_color': 'yellow'
   }
]

def printNames():
    for user in users:
        print(user["name"])

printNames()

def printHowMany():
    female=0
    male=0
    for user in users:
        gender = user["gender"]
        if gender == "female":
            female += 1
        elif gender == "male":
            male += 1
    #string formatting use the f at beginning of string
    print(f"There are {female} females and {male} males")

printHowMany()

def findById(id):
    for user in users:
        if user["id"]==id:
            print(user)
findById(1)