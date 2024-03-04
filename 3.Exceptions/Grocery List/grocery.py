grocery_list = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1

for item in sorted(grocery_list):
    print(grocery_list[item], item)

########### or #############

grocery_list = {}

try:
    while True:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
except EOFError:
    for item in sorted(grocery_list):
        print(grocery_list[item], item)
