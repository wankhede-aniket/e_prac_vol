"""
# Read Operation

f = open("data.txt", "r")
# syntax to oen file in python

print(f)
# only gives file information

print(f.read())
# read everything from your file

print(f.read(1))
# print only one character

print(f.readline(), end="")
# print only first line
print(f.readline(),end="")
# write this statement multiple time to next line of your data
"""

"""
# Write and Append Operation

f1 = open('write_file.txt', 'w')
# this command will create write_file.txt file for you

f1.write("Hey, Mr. Wankhede, How are you ")
# write the data in your file

f1.write("Hi Aniket ")
# adding extra data to file

f1 = open('write_file.txt', 'a')
# appending data in file
f1.write("Ms. Monika")
"""


"""
# Copy data from one file to another

for data in f:
    f1.write(data)
    
# this was not worked in my case but this is the one way to copy the data
"""

"""
# opening an image file in binary format

f2 = open('my_photo.jpg', 'rb')  # 'rb' for reading binary data
for hex_values in f2:
print(hex_values)
"""

"""
# opening a actual jpeg file

f3 = open('my_photo.jpg', 'rb')
f4 = open('my_pic.JPEG', 'wb')

for hex_values in f3:
    f4.write(hex_values)
"""

"""
# zip function : Mostly use in Socket Programming

names = ["Aniket", "Sourav", "Swapnil"]
comps = ["LTTS", "TCS", "Cybage"]

zipped =  list(zip(names, comps))
print(zipped)

zipped =  tuple(zip(names, comps))
print(zipped)

zipped =  dict(zip(names, comps))
print(zipped)

zipped =  set(zip(names, comps))
print(zipped)
"""
