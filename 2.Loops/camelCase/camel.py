camelCase = input("camelCase: ")
snake_case = ""
for chr in camelCase:
    if chr.isupper():
        snake_case += "_" + chr.lower()
    else:
        snake_case += chr

print("snake_case:", snake_case)
