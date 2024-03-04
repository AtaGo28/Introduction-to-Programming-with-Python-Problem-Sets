vowels = ["a", "e", "i", "o", "u"]

user_input = input("Input: ")
output = ""

for chr in user_input:
    if chr.lower() in vowels:
        output += chr.replace(chr, "")
    else:
        output += chr

print("Output:", output)
