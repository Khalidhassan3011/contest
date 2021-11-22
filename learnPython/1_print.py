import os

print("Hello world")

print("Hello", "world",  sep=" @ ")  # separate with @

print("Hello world", end="")  # without new line

l1 = "\nthis is a test \n Thank you"
print(l1)

print("hi" * 10)

print("hello " + os.getlogin())

print(f"hello, {os.getlogin()}! Great Work")
print(f"hello " * 5)

print(100)
print(f"hello: {100}")

# not worked
# print("hello " + 100);
# worked
print("hello " + str(100))

# print(1 + 2a)

print([1, 1, 2, 3, 4, ])  # list
print((1, 1, 2, 3, 4, ))  # set
print({"name ": "khalid", "age ": 25})

s = "0 1 2 3 4 5 6 7 8 9"
print(s[:])  # full
print(s[::])  # full
print(s[:-1])  # remove from last
print(s[1:])  # remove from fast
print(s[::-1])  # reverse

l2 = ["Geeks", "For", "Geeks"]
print(" ".join(l2))
