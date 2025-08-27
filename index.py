# Ask user to enter their first name
first_name = input("enter first name\n")
# Ask user to enter their last name 
last_name = input("enter last name\n")
# Print user's fullname in UPPERCASE
full_name = print((f"full name= {first_name} {last_name}\n").upper())
# e.g. If user full name is Jermie Asare it should rather print JERMIE ASARE


# Ask user to enter their first number 
first_number =input("enter first number\n")
# Ask user to enter their second number 
second_number =input("enter second number\n")
# Add the two number 
total= print(int(first_number) + int(second_number))
# Print the result




age = input("what's your age? \n")
if int(age) >=18 and int(age) >=45:
    print("You can have access")
else:
    print("You are not allowed here")




# Ask user an to input integer
# Find the integer modulo 2
# If the remainder is equal to 0 print Even 
# Else print Odd

integer = input("enter an integer \n")
if int(integer) % 2 ==0:
    print("even")
else:
    print("odd")


# Ask user to input their score as a number
# If score is between 90 to 100 (inclusive) print grade A
# If score is between 80 to 89 (inclusive) print grade B
# If score is between 70 to 79 (inclusive) print grade C
# If score is between 60 to 69 (inclusive) print grade D
# If score is between 0 to 59 (incllusive) print grade F

score = input("what's your score? \n")
if int(score) <=100 and int(score) >=90:
    print("grade A")
if int(score) <=89 and int(score) >=80:
    print("grade B")
if int(score) <=79 and int(score) >=70:
    print("grade C")
if int(score) <=69 and int(score) >=60:
    print("grade D")
if int(score) <=59 and int(score) >=0:
    print("grade F")



# Ask user to input their purchase amount as float
# If the purchase is 100 cedis or more apply 20% discount and print amount to pay
# If the purchase is 50cedis or more apply 10% discount and print amount to pay
# If the purchase is less than 50 cedis apply no discount and print amount to pay


#program to calculate the average of two numbers

# #take two numbers as input
num1 = float(input("enter first name\n"))
num2 = float(input("enter second name\n"))
# #declare the average variable
average= (num1 + num2)/2
# #declare average = (num1 + num2) / 2
print(f"the average is {(num1 + num2) /2}")
# #display the average

#OR
num1 = float(input("enter a number"))
num2 = float(input("enter a second number"))
print(f"the average of {num1} + {num2} is {(num1 + num2)/2}")


#program to calculate the average of two numbers

# #take two numbers as input
num1 = float(input("enter first name\n"))
num2 = float(input("enter second name\n"))
# #declare the average variable
average= (num1 + num2)/2
# #declare average = (num1 + num2) / 2
print(f"the average is {(num1 + num2) /2}")
# #display the average
print(f"the average of {num1} + {num2} is {(num1 + num2)/2}")
#accept an age input from the user and full name
full_name = input("enter your name\n")
age = int(input("enter your age\n"))
#if the age is less than 18 and the average is equal to 20,
#print {name}, you are not allowed 
if int(age) <18 and int(average) >=20:
  print(f"{full_name}, you are not allowed to vote")




# Ask user to input their purchase amount as float
# If the purchase is 100 cedis or more apply 20% discount and print amount to pay
# If the purchase is 50cedis or more apply 10% discount and print amount to pay
# If the purchase is less than 50 cedis apply no discount and print amount to pay

amount= float(input("enter a number\n"))
if amount >= 100:
    discount = 0.20 * amount
    amount_to_pay = amount - discount
    print(f"amount to pay is: {amount_to_pay}")
elif amount >= 50 and amount < 100:
    discount = 0.10 * amount
    print(f"amount to pay is: {amount - (0.10 * amount)}")
else:
    print("no discount for amount paid")


    

#Ask user to input the length of the 3 sides of a triangle
x =float(input("enter first side"))
y =float(input("enter second side"))
z =float(input("enter third side"))
#If all sides are equal print Equilateral
if x==y and y==z:
    print("Equilateral")
#If 2 sides are equal print Isosceles
elif x==y or y==z or x==z:
    print("Isosceles")
#If no sides are equal print Scalene
print("Scarlene")


file= open("tasks.txt", "r")
tasks= file.read().split("\n")
for task in tasks:
    print(f"{tasks.index(task) +1}.{task}")
    

file= open("tasks.txt", "r")
tasks= file.read().split("\n")
print(tasks)


#use loop to calculate the sum of the numbers below
numbers= [10, 5, 20, 8, 15]
total = 0
for num in numbers:
 total= total + num

 print("the sum is:",total)



#use loop to calculate the sum of the numbers below
numbers= [10, 5, 20, 8, 15]
total = 0
for num in numbers:
 total= total + num

print(total)


#open the file emails,txt in Read mode
#read and split the data using \n to get a list
#loop over the list of emails and print a generated username for each of them i.e username is all characters before the @

file= open("emails.txt" , "r")
emails= file.read().split("\n")
for email in emails:
    username = email.split("@")[0]
    print(username)


#define a register user function
def register_user(name, email, password):
    #check if user does not already exist
    #hash user password
    #validate inputs
    #check if user is not a robot
    #return response
    return "user register successfully"

response= register_user("Jermie Asare", "jermieasare@gmail.com", "098765432")


#define a function to add a task
def add_task(task):
    #save task to database
    #return response
    response= True


import add
import show
import update
import delete


add_task_response= add.add_task("Study")
print(add_task_response)

show_task_response= show.show_tasks()
print(show_task_response)

update_task_response= update.update_task("Study", "Code")
print(update_task_response)

delete_task_response= delete.delete_task("Study")
print(delete_task_response)



class Chat:
    def __init__( self, chatee, last_message, last_message_time):
        self.chatee =chatee
        self.last_message= last_message
        self.last_message_time= last_message_time

    def open(self):
        return f"you just opened the chat with {self.chatee} with last message {self.last_message} that was sent at {self.last_message_time}"
    

    from oop import Chat

chat_with_abena= Chat( "Abena Jollof", "Be guided!", "7:30 PM")
chat_with_michael= Chat("Michael Hammond", "Extend the portofolio deadline", "5:56 AM")
chat_with_0248653214= Chat("The Closer", "When are we ending the class","3:59 AM")


print(chat_with_abena.open())



class Chat:
    def __init__( self):
        self.chatee =input("who are you chatting with?\n")
        self.last_message= input("what was your last message?\n")
        self.last_message_time= input("when was the last message sent?\n")

    def __str__(self):
        return f"you are chatting with {self.chatee}"

    def open(self):
        return f"you just opened the chat with {self.chatee} with last message {self.last_message} that was sent at {self.last_message_time}"
    