# En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:
#   - toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
#   - si es par, evalúa un nuevo c0 como c0 ÷ 2;
#   - de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
#   - si c0 ≠ 1, salta al punto 2.
# La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

count=0
c0 = int(input("Ingresa un número entero positivo: "))
while c0 <= 0:
    print("El número debe ser un entero positivo mayor que cero.")
    c0 = int(input("Ingresa un número entero positivo: "))
else:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1
        count+=1
        print(int(c0))
print(f"Pasos =  {count}")