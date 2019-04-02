blocks = int(input("Enter number of blocks: "))
height = 0
inlayer = 1

while inlayer <= blocks:
    height += 1          # Se construye la capa
    blocks -= inlayer    # Se resta el numero de bloques usados al numero de bloques total
    inlayer += 1         # El numero de bloques para construir una nueva capa aumenta

print("Height of the pyramid:", height)