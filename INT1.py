##Programmer: Saphyre Rusch
##Date: 02/09/2022
##Description: This is a text-based adventure.
##For now, this is just a small story that will get longer each sprint

player = input("Welcome! Please enter your name: ")
friend = input("Next, please enter the name of a friend: ")
##I ask the user to give two names to make the game more personal.

print("You are on your way home from school when you hear a sound.")
print("You look around and realize the sound is coming from the bushes.")
bushes = input("You investigate. What do you expect to see? \n")
##The user has to input random answers to continue the story.

print("It's your friend,", friend, ", trying to spook you!")
print("After having a laugh, you both head to your house.")
print("You have a math test tomorrow, and they promised to help you study.")

##After reading about conditional statements from the Python textbook,
##I decided to add some in.
##This next series of conditionals is the user solving different math problems.
print("Let's power through these equations!")
math_equation = input("What is 5 + 4 * 3 // 2 - 1: ")
answer_1 = 5 + 4 * 3 // 2 - 1
if (int(math_equation) == answer_1):
    print("Nice! You must have been paying attention in class!")
else:
    print(friend, "sees you struggle, and gets ", answer_1)

print("Let's skip to division!")
math_division = input("What is the remainder from 30 divided by 4? ")
answer_2 = 30 % 4
if (int(math_division) == answer_2):
    print("Correct!", friend, "gives you a high-five!")
else:
    print(friend, "does the math, getting ", answer_2)

math_exponent = int(input("Time for exponents. What is 7 ** 3? "))
answer_3 = 7 ** 3
if (math_exponent == answer_3):
    print("This one stumped", friend, "so you got to help out this time.")
else:
    print("You check the back of the book, getting ", answer_3)

print("Last question. What is 545 / 24?")
math_decimal = float(input("For this one, you have to simplify to .000: "))
print("You ask for help this time because division is not your strong suit.")
print(friend, "does the math with you.")
answer = float(545 / 24)
print("It's a struggle, but you get: ", format(answer, '.3f'), sep='')
##Adding the decimal made this one more complicated.
##I thought it best to not add the conditional statment.

print("Congrats, ", player, ", you conquered your math homework!", sep='')
print("You send", friend, "home for the day, and you get rest for tomorrow.")
sleep = int(input("What time are you going to bed?\n"))
if (7 <= sleep <= 10): #if you pick between and including 7 and 10 PM
    print("Good idea. Tomorrow is going to be a great day!\n")
elif (sleep == 5 or sleep == 6):#if you pick between and including 5 and 6 PM
    print("You get too much sleep, and you wake up over-tired.\n")
elif (sleep <= 4 or sleep == 11 or sleep == 12):#if you pick between and including 11 PM and 4 AM
    print("Your mom gives you a lecture about not sleeping enough.\n")

print("Time for class! Your mom gives you a ride to school.")
print("You make it to your math class just in time.")
teacher_question = input("Your teacher asks you if you're ready. Are you?\n")
if (teacher_question == "no"):
    print("Your teacher shakes his head and sends you to your seat.")
elif (teacher_question == "yes"):
    print("Your teacher smiles, loving your confidence.")
else:
    print("You mumble " + teacher_question, "and rush to your seat.")
##I added the string operator to concatenate the two strings.

calculation = input("Time to find out if you passed! Did you pass or fail?\n")
print("101100110" * 50)
##I used this string operator to simulate computer calculations.

print("Congratulations!", end='')
print(" By some miracle, you passed your math test with a B!")
print("You give", friend, "a high-five, and you finish class with a grin.")

print("Thank you for playing along", player)
end_of_program = input("See you in the next adventure! Goodbye for now! \n")
print("You have reached the end of the adventure.")
##As the program gets built on, the adventure will be a longer story.


