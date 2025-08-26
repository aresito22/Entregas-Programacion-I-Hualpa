parcial_1 = float(input("Ingrese su nota del primer parcial: "))
parcial_2 = float(input("Ingrese su nota del segundo parcial: "))
parcial_3 = float(input("Ingrese su nota del tercer parcial "))

promedio_parciales = (parcial_1 + parcial_2 + parcial_3) / 3

calificacion_examen_final = float(input("Ingrese la nota del examen final: "))
calificacion_trabajo_final = float(input("Ingrese la nota de su trabajo final: "))

nota_final = (promedio_parciales * 0.55) + (calificacion_examen_final * 0.3) + (calificacion_trabajo_final * 0.15)

print(f"Su nota final es {nota_final}.")