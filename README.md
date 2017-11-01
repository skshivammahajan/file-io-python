# File Handling Cheat Sheet in Python

filename = "hello.txt"
file = open(filename, "r")
for line in file:
   print line,
# Read ()
The read functions contains different methods, read(),readline() and readlines()

read()		#return one big string

readline	#return one line at a time

readlines	#returns a list of lines
# Write ()
This method writes a sequence of strings to the file.

write ()	#Used to write a fixed sequence of characters to a file

writelines()	#writelines can write a list of strings.
# Append ()
The append function is used to append to the file instead of overwriting it.

To append to an existing file, simply open the file in append mode ("a"):
# Close()
When you’re done with a file, use close() to close it and free up any system
resources taken up by the open file
