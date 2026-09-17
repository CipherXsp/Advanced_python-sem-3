# Open input file
f1 = open("APP1.txt", "r")

# Read all lines
lines = f1.readlines()

# Close input file
f1.close()

# Count total number of lines
print("Total No of line in file APP1.txt:", len(lines))

# Display all lines
print("Contents of list lines:", lines)

# Extract first two lines
two_lines = lines[:2]

# Display first two lines
print("First two lines:")

for i in two_lines:
    print(i)

# Create output file
f2 = open("output.txt", "w")

# Write first two lines into output file
f2.writelines(two_lines)

# Close output file
f2.close()

print("\nFirst two lines from APP1.txt are written in file output.txt")
