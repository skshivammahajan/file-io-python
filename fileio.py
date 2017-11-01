# Opening a file
file_object = open("testfile.txt","w")
# Writing in a file
file_object.write("Hello Python!\n")
file_object.write("Python Bang Bang!!")

# write multiple lines to a file at once: 
lines_of_text = ["One line of text here", "and another line here", "and yet another here", "and so on and so forth"] 
file_object.writelines(lines_of_text) 
print(file_object.closed)

# Closing a file
file_object.close()
 # What this does is close the file completely, terminating resources in use, in turn freeing them up for the system to deploy elsewhere. 
print(file_object.closed)


file_read = open("testfile.txt", "r")
# Reading file
# read the first five characters of stored data and return it as a string: 
print (file_read.read(5))
#  read a file line by line
print(file_read.readline())
#  return only the second line in the file,
print(file_read.readline(2))
# Read the file at once
print(file_read.read())
# return every line in the file, properly separated in the form of list
print(file_read.readlines())

# Looping over a file object
# return all the lines from a file in a more memory efficient, and fast manner, you can use the loop over method
file_read = open("testfile.txt", "r")
for line in file_read:
	print(line)

 # append a file: 
fh = open("testfile.txt", "a") 
fh.write("We Meet Again World") 
fh.close 

# With Statement
# One bonus of using this method is that any files opened will be closed automatically after you are done. This leaves less to worry about during cleanup. 
with open("testfile.txt") as file:
	print(file.read())
# we didn’t use the “file.close()” method because the with statement will automatically call that for us upon execution
