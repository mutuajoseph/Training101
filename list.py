# Using append to output data
# The first thing to do is to append it the output it
# Append refers to adding an existing dataset to another existing dataset

daysOfTheWeek = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

daysOfTheWeek.append("val")
print("DAYS OF THE WEEK = ",daysOfTheWeek)

# CLEAR refers to removing an existing list in the memory allocation
daysOfTheWeek.clear()

# EXTEND refers to merging two lists into one whole list

list1 = [0,1]
list2 = [2,3]

daysOfTheWeek.append(list1)
print(daysOfTheWeek)


