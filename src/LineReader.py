#
# def ReadFromFile(filename):

#     content = open(filename, "r")
#     line = content.readline()
#     print("line:", line)
#     return line


import os

def ReadFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("Bad File")
    content = open(filename, "r")
    line = content.readline()
    print("line:", line)
    return line
