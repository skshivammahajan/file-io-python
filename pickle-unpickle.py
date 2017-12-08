"""
Reference : https://pythontips.com/2013/08/02/what-is-pickle-in-python/
"""
import pickle

# Pickle
# Python object i.e list
a = ['test value', 'test value 2', 'test value 3']

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name, 'wb')
print(fileObject)
# this writes the object a to the
# file named 'testfile'
pickle.dump(a, fileObject)
# here we close the fileObject
fileObject.close()

# Unpickle
# we open the file for reading
fileObject = open(file_Name, 'rb')
print(fileObject)
# load the object from the file into var b
b = pickle.load(fileObject)
print(a == b)
print(b)
