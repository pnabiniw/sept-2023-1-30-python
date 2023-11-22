# We can open, close and manipulate files using python
# Files in python can be opened in different modes
# r (Read)
# w (Write)
# a (Append)
# r+ (Read and write)
# w+ (Write and Read)
# a+ (Append and Read)
# x (Exclusive Write mode)

fp = open("message.txt", "w")
fp.write("Hello World")
fp.close()

fp = open("message.txt", "r")
data = fp.read()
fp.close()
print(data)


fp = open("message.txt", "a")
fp.write("\nI'm learning Python")
fp.close()


fp = open("message.txt", "r+")
data = fp.read()
print(data)
fp.write("\nThis is a new message")
fp.close()


fp = open("message.txt", "w+")
fp.write("\nMessage Continue")
fp.seek(0)
data = fp.read()
fp.close()
print(data)


fp = open("message.txt", "x")
fp.write("New Message")
fp.close()


# Closing the file is important as it protects the system from memory leakage.
# But sometimes we may forget to close the file
# So, it is better to open a file with context manager

with open("message.txt", "r") as fp:
    data = fp.read()

# While getting out from "with" block indentation, the file is closed automatically
print(data)

with open("message.txt", "w") as fp:
    fp.write("Hello World")
