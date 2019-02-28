# Using a reverse function create a function that does take in a name and reverses



# Define the function as step number one
def reverseMyName(name):
    x = name[::-1]
    return x

# Input the name of the person
myName = input("What is your name")

#Call the function to print out the reversed word
reversedName = reverseMyName(myName)
print(reversedName)