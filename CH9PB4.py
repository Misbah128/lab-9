# Syed Hussain
# 09/04/2022
# Problem 4 :- Creating a while loop that initializes a counter at 0 and will run until the counter reaches 50.
# If the value of the counter is divisible by 10, append the value to the list called tens.
# Confirm the list results using a print statement.

#The changed question: 
# This program uses a while loop
# It creates a list called L that contains the numbers 10 to 20.
# On each iteration, the loop appends the current value of a counter variable to the list "L".
# and then increase the counter by 1.
# The while loop stops once the counter variable is greater than 20 and prints the final list "L".

counter = 0
tens=[]
while(counter<=50):
    if counter % 10 == 0:
        tens.append(counter)
    counter = counter + 1

print(tens)
