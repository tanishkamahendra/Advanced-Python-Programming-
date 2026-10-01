f = open("input.txt", "w")

f.write("Line 1: This is the first line.\n")
f.write("Line 2: This is the second line.\n")
f.write("Line 3: This is the third line.\n")
f.write("Line 4: This is the fourth line.\n")

f.close()

f = open("input.txt", "r")
lines = f.readlines()
f.close()

print("Total number of lines:", len(lines))

first_two = lines[:2]

f = open("output.txt", "w")
f.writelines(first_two)
f.close()

print("Extracted lines written to output.txt")

f = open("output.txt", "r")
print("Content of output.txt:")
print(f.read())
f.close()