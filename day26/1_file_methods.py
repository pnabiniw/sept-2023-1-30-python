filename = "message.txt"

# with open(filename, "w") as fp:
#     fp.write("Hello World\nI'm Learning Python")

# read()
# write()
# seek()
# readline()
# readlines()
# tell()
# writelines()

with open(filename, "r") as fp:
    data = fp.read()  # reads the content of the file
    print(data)
    fp.seek(0)  # changes the cursor of the file in the desired location
    data = fp.read()
    print(data)

    fp.seek(0)
    data = fp.readline()
    print(data)  # Hello World

    fp.seek(13)
    data = fp.readline()
    print(data)  # I'm Learning Python

    fp.seek(0)
    data = fp.readlines()
    print(data)  # ["Hello World\n", "I'm learning Python"]

    print(fp.tell())  # 32. It tells the location of the cursor in the file


message = ["Python is a high level language\n", "I'm Learning python"]
with open(filename, "w") as fp:
    fp.writelines(message)
