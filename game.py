from random import randint

print "Hello! Let's play a game"# Put your code here

name = raw_input("What is your name?")
random_number = randint(0, 101)
#print random_number

count = 0

while True:
    guessed_num = raw_input("Please guess a number between 1 and 100: ")
    guessed_num = int(guessed_num)
    #print guessed_num
    if guessed_num > random_number:
        count = count + 1
        print "Your guess is too high, try again."
    elif guessed_num < random_number:
        count = count + 1
        print "Your guess is too low, try again."
    else:
        count = count + 1
        print "Congratuations, {0} you found my number in {1} tries.".format(name, count)
        break

