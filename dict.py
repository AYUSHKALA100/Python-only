

# Word Count in Sentence
# Take a sentence input from the user and count how many times each word occurs. Store the result in a dictionary.

word=input("Enter the sentence\n")

for i in range(len(word)):
 char=list(word[i:i+1])
 print(char)
 char.append(char[i])

str(char)
for item in char:
  
  no=char.count(item)
  print(item,"\n the count is ",no)



# result={}


# Menu Card System
# Create a food menu with dishes as keys and prices as values. Ask the user to enter 3 dish names and print the total bill.



# Student Marks Record
# Create a dictionary with student names as keys and their marks as values. Add a new student, update an existing one, and find the average marks.
# result = {
#     "Aman":84,
#     "Ayush":90,
#     "Amul":78,
#     "rahul":80,
#     }
# result.update({"komal":90, "Aman":100})
# print(result)

# for item in result:
#     total=result[item]
#     total+=total

# average=total/5
# print(average)

