total_hombres = int(input("Hombres: "))
total_mujeres = int(input("Mujeres: "))
total_estudiantes = total_hombres + total_mujeres

porcentaje_hombres = (total_hombres/total_estudiantes) * 100
porcentaje_mujeres = (total_mujeres/total_estudiantes) * 100

print(f"Porcentaje de hombres: {porcentaje_hombres}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres}%")

