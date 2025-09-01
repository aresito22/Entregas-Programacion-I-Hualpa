monto = int(input("Ingrese el monto del préstamo: "))
cuotas = int(input("Ingrese la cantidad de cuotas (12-72): "))
interes = 0.02

es_veraz = input("¿Está en el veraz? (s/n): ")
es_veraz = es_veraz.lower()
if es_veraz == 's':
    print("No puede acceder al préstamo si está en el veraz.")
else:
    total_a_devolver = monto * (1 + interes) ** cuotas
    cuota_mensual = total_a_devolver / cuotas
    
    ingresos_netos_mensuales = int(input("Ingrese sus ingresos netos mensuales: "))
    
    if ingresos_netos_mensuales < (cuota_mensual * 0.3):
        print("No puede acceder al préstamo ya que su ingreso neto mensual es menor al 30% de la cuota mensual.")
    else:
        print(f"Su cuota mensual será de: {round(cuota_mensual, 2)}")
        print(f"El total a devolver será de: {round(total_a_devolver, 2)}")