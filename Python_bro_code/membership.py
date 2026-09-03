# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, dictionary)
#                        1. in
#                        2. not in

word = "APPLE" # Membership operator used in string

letter = input("Guess a letter in the secret letter: ")

# Boolean value is returned for these operators

if letter in word:
    print(f"Yes, {letter} is in the word")
else:
    print(f"Sorry, {letter} is not in the word")
    
print("----------------------------------------------")

students = {"Spongebob", "Patrick", "Sandy"} # Membership operator used in set

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student.")
else:
    print(f"{student} was not found")
    
print("----------------------------------------------")

grades = {"Sandy": "A",         # Membership operator used in set
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}") # If using f-string then can do this!!! 
else:
    print(f"{student} was not found")

print("----------------------------------------------")

email = "BroCode@gmail.com" # To check whether something is there or not...

if "@" and "." in email:
    print("Valid Email!")
else:
    print("Invalid Email")
    
print("----------------------------------------------")

email_id = input("Enter your E-mail Id: ")

while ("@" and ".") not in email_id:
    print("Email Id is invalid!!!")
    email_id = input("Re-Enter your E-mail Id: ")
print(f"Your entered email is: {email_id}")