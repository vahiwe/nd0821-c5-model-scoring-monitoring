## instantiating a variable that will store your final answer
finalanswer=0

## create a loop that iterates over all the numbers we're interested in, and adds each of them to the final answer
for i in range(10000):
    finalanswer=finalanswer+i

## you can print the final answer
print(finalanswer)