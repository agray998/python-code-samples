s1 = "Hello"
s2 = ","
s3 = "world"
f = open("demo.txt", "w")
print(s1, s2, s3, sep="...", end="", file=f)
f.close()

'''
s4 = input("Enter your name: ")
print("Hello,", s4)
'''

x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(x + y)