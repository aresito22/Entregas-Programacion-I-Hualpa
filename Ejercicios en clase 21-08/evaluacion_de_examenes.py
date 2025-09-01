examenes_a = int(input())
examenes_b = int(input())
examenes_c = int(input())

tiempo_a = examenes_a * 5
tiempo_b = examenes_b * 8
tiempo_c = examenes_c * 6

tiempo_total = tiempo_a + tiempo_b + tiempo_c

horas = tiempo_total // 60
minutos = tiempo_total % 60

print(f"{horas} horas {minutos} minutos")