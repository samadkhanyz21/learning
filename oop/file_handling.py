# How to save a file
# w writes the data in text file that we created.
import string

f = open('test_file.txt', 'w')
f.write("This is our 1st line of code.\n")
f.write("This is our 2nd line of code.\n")
# Always close file after creating one
f.close()

# To add data to the file use a for append.
f = open('test_file.txt', 'a')
f.write("See this is appended not over written.")
# Always close file after creating one
f.close()

# To read a file use r.
f = open('test_file.txt', 'r')
# this way stores the data into our memory
# if file is large then it will take a lot of our memory
# rather save the read file to a variable.
# the data will be printed inform of string and
# will need to store the data in less momory.
# f.read(print(f.read()))
file_content = f.read()
print(file_content)
f.close()

# f.open('test_file.txt','r')
# # in order to get a specific line from our saved file use:
# file_line = f.readline()
# print(file_line, end='')
# f.close()

# Use context manager much better.
# Close by itself not to worry for close attribute.
with open('test_file.txt', 'r') as f:
    for line in f.readlines():
        print(line)