blocks = int(input("Enter number of blocks: "))
height = 0

for i in range(2,blocks):
    height = i
    i -= 1

print("Height of the pyramid:",height)