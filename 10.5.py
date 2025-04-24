# Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.

with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        u=line.upper()
        outfile.write(u)

print("Content copied to 'output.txt' in uppercase.")
