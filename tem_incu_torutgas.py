print("""\n**** REGISTRO INFORMACION ****\n""")


def evaluar_tem(tem):
    if tem < 26:
        return("T. baja")
    elif 26 < tem < 34:
        return("T. normal")
    elif tem > 34:
        return("T. alta")

tem = float(input("Ingrese la temperatura: "))
print(evaluar_tem(tem))
