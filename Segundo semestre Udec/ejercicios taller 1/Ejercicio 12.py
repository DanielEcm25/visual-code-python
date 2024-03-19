'''Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los
datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último,
mostrar la lista nueva con los nuevos datos.'''

listaOriginal = [1,2,3,4,5,6,7,8,9,10]
ListaFinal = []
for i in listaOriginal:
    if i/4==1 or i/7==1 or i/9==1:
        a=i*2
        ListaFinal.append(a)
for j in ListaFinal:
    print(f"{j//2} * 2 = {j*2}")
