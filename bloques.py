# Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. 
# Están construyendo una pirámide. Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana.
#  La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

amount_of_blocks = int(input("¿Cuántos bloques de madera tienes? "))
layers = 0
while amount_of_blocks >= layers + 1:
    layers += 1
    amount_of_blocks -= layers  
print(f"Puedes construir una pirámide con {layers} capas. Sobran {amount_of_blocks} bloques.")