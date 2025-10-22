# def greet():
#     return f"Hello, {username}!"
# print(greet())

def greet(username):
    return f"Hello, {username}!"
print(greet())


# counts = {"a":1, "b":2, "c":3}
# for k in counts:
#     if counts[k] % 2 == 1:
#         del counts[k]    
# print(counts)

counts = {"a":1, "b":2, "c":3}
counts2 = {}
for k,v in counts.items():
    counts2[k] = v
for k in counts2:
    if counts[k] % 2 == 1:
        del counts[k]
print(counts)



# text = "debugging"
# print(text.push("!"))

text = "debugging"
print(text + "!")



# nums = [1, 2, 3]
# for i in range(0, len(nums)):
#     print(nums[i + 1])

nums = [1, 2, 3]
for i in range(len(nums)):
    print(nums[i])



# config = {"host": "localhost", "port": 5432}
# print(config["username"])

config = {"host": "localhost", "port": 5432}
print(config["host"])



# age = "12"
# print(age + 5)

age = 12
print(age + 5)



# user_input = "12.5"
# print(int(user_input))

user_input = "12.5"
print(float(user_input))



# def ratio(a, b):
#     return a / b
# print(ratio(10, 0))

def ratio(a, b):
    if b == 0:
        return "cannot devide by zero"
    return a / b
print(ratio(10, 0))



# import jsonn
# print(json.dumps({"ok": True}))

import json
print(json.dumps({"ok": True}))



# def down(n):
#     return down(n - 1)
# print(down(5))

def down(n):
    if n == 0:
        return n
    return down(n - 1)
print(down(5))



x = 5
while x > 0:
    print(x)
# x never changes



# def add_item(item, bucket=[]):
#     bucket.append(item)
#     return bucket

# print(add_item("a"))
# print(add_item("b"))

def add_item(item):
    bucket=[]
    bucket.append(item)
    return bucket

print(add_item("a"))
print(add_item("b"))
print(add_item("c"))



funcs = []
for i in range(3):
    funcs.append(lambda: print(i))

for f in funcs:
    f()  # Expected 0,1,2; what happens?

Find & fix: Bind current i at creation time.



# items = [1, 2, 3, 4, 5]
# for x in items:
#     if x % 2 == 0:
#         items.remove(x)
# print(items)


items = [1, 2, 3, 4, 5]
items_copy = items[:]
for x in items_copy:
    if x % 2 == 0:
        items.remove(x)
print(items)



# a = [1, 4, 9]
# b = [2, 3, 6, 8]
# i, j = 0, 0
# merged = []
# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         merged.append(a[i])
#         i += 1
#     else:
# 	  merged.append(b[j])
#         j += 1
# print(merged)
# Find & fix : The Expected output is:
# [1, 2, 3, 4, 6, 8, 9]


a = [1, 4, 9]
b = [2, 3, 6, 8]
i, j = 0, 0
merged = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1
merged += a[i:] + b[j:]
print(merged)



# for i in range(3):
#     j = 0
#     j += 1
#     print(j)

j = 0
for i in range(3):
    j += 1
    print(j)



full_name = "Avi"
print(f"User: {full_name}")



# data = [10, 20, 30, 40]
# total = 0
# for i in range(len(data) - 1):
#     total += data[i]
# print("Total:", total)  # Why is 40 missing?


data = [10, 20, 30, 40]
total = 0
for i in range(len(data)):
    total += data[i]
print("Total:", total)  # Why is 40 missing?