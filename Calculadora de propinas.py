# Solicitar al usuario el total de la cuenta y el porcentaje de propina que desea dejar
total_cuenta = float(input("Ingrese el total de la cuenta: $"))
porcentaje_propina = int(input("Ingrese el porcentaje de propina que desea dejar (%): "))

# Calcular la cantidad de propina a dejar y el total de la cuenta, incluyendo la propina
propina = total_cuenta * porcentaje_propina / 100
total_cuenta_con_propina = total_cuenta + propina

# Mostrar los resultados al usuario
print(f"La cantidad de propina a dejar es: ${propina:.2f}")
print(f"El total de la cuenta, incluyendo la propina, es: ${total_cuenta_con_propina:.2f}")