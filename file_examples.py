# opening a file
# file = open("demo.txt", "w") # other modes: (r)ead, (r)ead-(w)rite, (a)ppend
# file.write("Hello World")
# file.close()

# file2 = open("demo.txt", "r")
# contents = file2.read(5)
# print(file2.tell())
# file2.seek(file2.tell() + 8)
# print(file2.read(5))
# file2.close()
# print(contents)

with open("demo.txt", "r") as file:
    for no, line in enumerate(file):
        print(no, "\t", line, end="")